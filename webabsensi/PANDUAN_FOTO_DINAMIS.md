# Panduan Mengatur Ukuran & Posisi Foto Berdasarkan Jenjang

Jika orientasi atau desain bingkai foto untuk jenjang "KB" berbeda (sehingga butuh ukuran atau posisi yang secara khusus berbeda dari jenjang lainnya), kita bisa menambahkan *class* CSS bersyarat (conditional class) khusus untuk jenjang tersebut.

Silakan ikuti langkah-langkah berikut di file `adminapp/templates/cetak_id_card.html`:

## Langkah 1: Tambahkan Class Khusus di Tag Foto
Cari bagian HTML yang memunculkan foto (bingkai foto). Anda perlu menambahkan deteksi otomatis apakah jenjangnya 'KB' di dalam atribut `class`.

Ubah baris `<img ... class="foto-siswa">` menjadi:
```html
        <!-- FOTO -->
        {% if siswa.foto %}
            <img src="{{ siswa.foto.url }}" alt="Foto Siswa" class="foto-siswa {% if siswa.kelas.jenjang == 'KB' %}foto-kb{% endif %}">
        {% else %}
            <!-- Kalau tidak ada foto -->
            <div class="foto-siswa {% if siswa.kelas.jenjang == 'KB' %}foto-kb{% endif %}" style="background-color: rgba(255,255,255,0.7); display: flex; justify-content: center; align-items: center; color: #333; font-weight: bold;">
                Belum Upload Foto
            </div>
        {% endif %}
```

## Langkah 2: Buat Kode CSS Baru Bernama `.foto-kb`
Scroll ke atas atau cari tag `<style>`. 
Temukan blok CSS milik `.foto-siswa` (pengaturan standar). Tepat **di bawah kode tersebut**, tambahkan pengaturan overriding khusus untuk `.foto-kb`.

Contoh letak dan penulisannya:
```css
        /* FOTO SISWA (STANDAR UMUM) */
        .foto-siswa {
            position: absolute;
            top: 33.1%; 
            left: 22.7%;  
            width: 29.3mm; 
            height: 32.7mm; 
            border-radius: 3mm; 
            object-fit: cover; 
            z-index: 1;
        }

        /* --- TAMBAHKAN BAGIAN INI --- */
        /* FOTO SISWA KHUSUS JENJANG KB */
        .foto-kb {
            top: 35%;      /* Ganti sesuai posisi Y (atas-bawah) kotak foto di template KB */
            left: 25%;     /* Ganti sesuai posisi X (kiri-kanan) di template KB */
            width: 25mm;   /* Ganti ukuran lebarnya */
            height: 35mm;  /* Ganti ukuran tingginya */
            /* border-radius: 5mm; Jika lengkungannya juga beda, tambahkan ini */
        }
        /* ---------------------------- */
```

## Selesai!
Simpan file (Ctrl+S / Cmd+S). Aturan CSS akan saling menimpa; yang artinya property *default* akan berjalan, namun saat website mendeteksi jenjangnya adalah **KB**, sistem akan menggunakan angka `width`, `height`, `top`, dan `left` milik class `.foto-kb`. 

Sambil edit angka-angkanya, Anda tinggal `Refresh / F5` berulang kali di halaman browser (*print preview ID Card siswa KB*) untuk mengepaskan posisinya.