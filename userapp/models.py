from django.db import models
import datetime


class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=50, unique=True)

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
    created_at = models.DateTimeField(auto_now_add=True)

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
