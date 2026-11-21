from django.db import models
from django.core.files.base import ContentFile
from PIL import Image, ImageOps
import datetime
import io

try:
    from rembg import remove
except ImportError:
    remove = None


def process_student_photo(image_field, size=600, top_pad=0.04):
    image_field.seek(0)
    img = ImageOps.exif_transpose(Image.open(image_field)).convert("RGBA")
    if remove:
        nobg = remove(img)
    else:
        nobg = img

    # Cek apakah gambar memiliki transparansi
    alpha = nobg.split()[-1]
    has_transparency = alpha.getextrema() != (255, 255)

    if has_transparency:
        bbox = nobg.getbbox()
        if bbox:
            nobg = nobg.crop(bbox)
        w, h = nobg.size
        # Zoom subjek agar proporsional di ID Card (isi ~92% tinggi dan max 96% lebar)
        target_h = int(size * 0.92)
        scale_by_h = target_h / h
        # Jika setelah di-scale tingginya, lebarnya melebihi kanvas, scale berdasarkan lebar
        if int(w * scale_by_h) > int(size * 0.96):
            scale = (size * 0.96) / w
        else:
            scale = scale_by_h
            
        nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
        resized = nobg.resize((nw, nh), Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        # Tempel pas menempel di bagian bawah (y = size - nh), rata tengah horizontal
        canvas.paste(resized, ((size - nw) // 2, size - nh), resized)
    else:
        # Foto biasa (tanpa hapus background): center-crop persegi proporsional
        w, h = nobg.size
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        cropped = nobg.crop((left, top, left + min_dim, top + min_dim))
        canvas = cropped.resize((size, size), Image.Resampling.LANCZOS)

    buf = io.BytesIO()
    canvas.save(buf, format="PNG")
    return ContentFile(buf.getvalue())


class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=50, unique=True)

    JENJANG_CHOICES = [
        ('KB', 'KB'),
        ('TK', 'TK'),
        ('PKBM', 'PKBM'),
        ('TPQ', 'TPQ'),
        ('MADIN', 'MADIN'),
    ]
    jenjang = models.CharField(max_length=15, choices=JENJANG_CHOICES, default='TK')
    # Jadwal Spesifik per Kelas
    jadwal_masuk_mulai = models.TimeField(
        default=datetime.time(6, 0), verbose_name="Mulai Absen Masuk")
    jadwal_masuk_akhir = models.TimeField(default=datetime.time(
        7, 15), verbose_name="Batas Terlambat Masuk")
    jadwal_pulang_mulai = models.TimeField(
        default=datetime.time(14, 0), verbose_name="Mulai Absen Pulang")
    jadwal_pulang_akhir = models.TimeField(
        default=datetime.time(17, 0), verbose_name="Batas Absen Pulang")

    def __str__(self):
        return self.nama_kelas


class JadwalSesi(models.Model):
    kelas = models.ForeignKey(
        Kelas, on_delete=models.CASCADE, related_name='sesi_jadwal')
    nama_sesi = models.CharField(max_length=50)  # Contoh: "Pagi", "Sore"

    jam_masuk_mulai = models.TimeField(
        default=datetime.time(6, 0), verbose_name="Mulai Absen Masuk")
    jam_masuk_akhir = models.TimeField(
        default=datetime.time(7, 15), verbose_name="Batas Terlambat Masuk")

    jam_pulang_mulai = models.TimeField(
        default=datetime.time(14, 0), verbose_name="Mulai Absen Pulang")
    jam_pulang_akhir = models.TimeField(
        default=datetime.time(17, 0), verbose_name="Batas Absen Pulang")

    def __str__(self):
        return f"{self.kelas.nama_kelas} - {self.nama_sesi}"


class WaktuOperasional(models.Model):
    # Singleton Model (hanya 1 baris data)
    jam_masuk_mulai = models.TimeField(default=datetime.time(6, 0))
    jam_masuk_akhir = models.TimeField(default=datetime.time(8, 0))
    jam_pulang_mulai = models.TimeField(default=datetime.time(12, 0))
    jam_pulang_akhir = models.TimeField(default=datetime.time(17, 0))

    # Override save agar hanya ada 1 instance
    def save(self, *args, **kwargs):
        self.pk = 1
        super(WaktuOperasional, self).save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name_plural = "Waktu Operasional"

# Model untuk data Siswa


class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=20, unique=True, verbose_name="NIK/NIS")
    # Mengubah CharField menjadi ForeignKey ke model Kelas
    kelas = models.ForeignKey(
        Kelas, on_delete=models.SET_NULL, null=True, related_name='siswa_list')
    no_telepon = models.CharField(max_length=15)
    # RFID UID boleh kosong (null=True) agar bisa input data siswa duluan tanpa kartu
    rfid_uid = models.CharField(
        max_length=50, unique=True, verbose_name="RFID UID", null=True, blank=True)
    foto = models.ImageField(upload_to='foto_siswa/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.foto and not self.foto._committed:
            self.foto.save(f"{self.nik}.png", process_student_photo(self.foto), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nama} ({self.kelas})"

# Model untuk mencatat absensi (Masuk & Keluar)


class Absensi(models.Model):
    siswa = models.ForeignKey(
        Siswa, on_delete=models.CASCADE, related_name='absensi_siswa')
    sesi = models.ForeignKey(
        JadwalSesi, on_delete=models.SET_NULL, null=True, blank=True, related_name='absensi_sesi')
    tanggal = models.DateField(auto_now_add=True)
    hari = models.CharField(max_length=20, blank=True)
    jam_masuk = models.TimeField(auto_now_add=True)
    jam_keluar = models.TimeField(null=True, blank=True)
    status_kehadiran = models.CharField(
        # Telat, Tepat Waktu, dll
        max_length=50, default='Hadir', blank=True, verbose_name="Status Kehadiran")
    # Helper field untuk sorting real-time
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Otomatis isi nama hari jika belum diisi
        if not self.id and not self.hari:
            # Gunakan locale indo jika memungkinkan, atau translate manual nanti
            import locale
            try:
                # locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')
                # Hati-hati dengan locale di server yang belum terinstall
                pass
            except:
                pass
            self.hari = datetime.datetime.now().strftime("%A")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.siswa.nama} - {self.tanggal} ({self.status_kehadiran})"

# Model Untuk Log semua scan (Berhasil maupun Gagal) untuk keperluan display


class RfidLog(models.Model):
    rfid_uid = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[(
        'success', 'Berhasil'), ('unknown', 'Tidak Dikenal')])
    keterangan = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.rfid_uid} - {self.status} - {self.timestamp}"
