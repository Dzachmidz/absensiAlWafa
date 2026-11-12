# Panduan Membuat Background ID Card Dinamis (Berdasarkan Jenjang)

Karena Anda sudah menambahkan kolom `jenjang` pada tabel `Kelas` di file `models.py`, kita bisa memanfaatkannya untuk memunculkan background ("bg") yang berbeda-beda saat mencetak ID Card.

Berikut adalah alur langkah-demi-langkahnya:

## Langkah 1: Siapkan Semua File Gambar Background
Pastikan Anda sudah meng-copy semua gambar background ke dalam folder `static/`.
Ganti nama filenya agar rapi dan mudah dikenali, contoh:
- `bg_kb.png`
- `bg_tk.png`
- `bg_pkbm.png`
- `bg_tpq.png`
- `bg_madin.png`

## Langkah 2: Hapus Background Statis di CSS
Buka file **`adminapp/templates/cetak_id_card.html`**.
Cari bagian selector CSS `.id-card-wrapper` di dalam tag `<style>`.
**HAPUS** (atau jadikan komentar) baris `background-image` karena kita akan memindahkannya langsung ke HTML.

Ubah dari yang asalnya begini:
```css
        .id-card-wrapper {
            position: relative;
            width: 54mm; 
            height: 85mm; 
            background-color: #fff;
            
            /* HAPUS BARIS INI: */
            background-image: url('/static/bg_pkbm.png'); 
            
            background-size: 100% 100%; 
            /* ... sisa kode lainnya ... */
        }
```

## Langkah 3: Tambahkan Logika If-Else pada Tag `<div>` Pembungkus
Masih di file `cetak_id_card.html`, scroll ke bawah ke bagian HTML-nya.
Cari baris ini:
```html
    <!-- PEMBUNGKUS KARTU -->
    <div class="id-card-wrapper">
```

**UBAH** baris tersebut menjadi logika If-Else dari Django seperti ini:

```html
    <!-- PEMBUNGKUS KARTU -->
    <div class="id-card-wrapper" style="
        {% if siswa.kelas.jenjang == 'KB' %}
            background-image: url('/static/bg_kb.png');
        {% elif siswa.kelas.jenjang == 'TK' %}
            background-image: url('/static/bg_tk.png');
        {% elif siswa.kelas.jenjang == 'PKBM' %}
            background-image: url('/static/bg_pkbm.png');
        {% elif siswa.kelas.jenjang == 'TPQ' %}
            background-image: url('/static/bg_tpq.png');
        {% elif siswa.kelas.jenjang == 'MADIN' %}
            background-image: url('/static/bg_madin.png');
        {% else %}
            background-image: url('/static/bg_pkbm.png'); <!-- Default jika kosong -->
        {% endif %}
    ">
```
*Catatan: Pastikan nama file di dalam `url(...)` sama persis dengan yang Anda copy ke folder `static/`!*

## Selesai!
Sekarang jika Anda klik Cetak ID Card:
- Jika siswa tersebut berada di kelas yang jenjangnya **TK**, maka yang muncul adalah `bg_tk.png`.
- Jika kelas siswa ada di jenjang **PKBM**, maka yang termuat adalah `bg_pkbm.png`.
- dst.

Simpan filenya (Ctrl+S / Cmd+S) dan silahkan ujicoba dengan mencetak ID Card dari siswa yang berbeda jenjang.