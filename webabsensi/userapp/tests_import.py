import io
import openpyxl
from django.test import TestCase, override_settings

from adminapp.views import _norm_phone, _norm_rombel, _parse_siswa_excel, _run_import_siswa
from userapp.models import Kelas, Siswa


def _make_excel(rows):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Daftar Peserta Didik'])
    ws.append([])
    ws.append(['No', 'Nama', 'NIPD', 'JK', 'NISN', 'Tempat Lahir', 'NIK', 'HP', 'Telepon', 'Rombel Saat Ini'])
    for row in rows:
        ws.append(row)
    buf = io.BytesIO()
    wb.save(buf)
    buf.seek(0)
    return buf


class ImportSiswaTest(TestCase):
    def test_norm_phone(self):
        self.assertEqual(_norm_phone('087856424337'), '6287856424337')
        self.assertEqual(_norm_phone('+62 812-3456-789'), '628123456789')
        self.assertEqual(_norm_phone('8123456789'), '628123456789')
        self.assertEqual(_norm_phone('628123456789'), '628123456789')
        self.assertEqual(_norm_phone(None), '-')

    def test_norm_rombel(self):
        self.assertEqual(_norm_rombel('  al   idrisi '), 'AL IDRISI')

    def test_parse_skips_header_row_and_reads_columns(self):
        buf = _make_excel([
            [1, 'ACHMAD FAHRI', None, 'L', '3212661422', 'SIDOARJO', '3515152912210001', '087856424337', None, 'AL IDRISI'],
            [2, 'Nama', None, 'L', None, None, None, None, None, None],
            [3, 'BUDI', None, 'L', '3212.0', None, None, None, '081938105553', 'al jahiz'],
            [None, None, None, None, None, None, None, None, None, None],
        ])
        items = _parse_siswa_excel(buf)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['nama'], 'ACHMAD FAHRI')
        self.assertEqual(items[0]['nisn'], '3212661422')
        self.assertEqual(items[0]['no_telepon'], '6287856424337')
        self.assertEqual(items[0]['rombel'], 'AL IDRISI')
        self.assertEqual(items[1]['nisn'], '3212')
        self.assertEqual(items[1]['no_telepon'], '6281938105553')
        self.assertEqual(items[1]['rombel'], 'AL JAHIZ')

    def test_import_uses_rombel_per_row_and_updates_existing(self):
        kelas_a = Kelas.objects.create(nama_kelas='AL IDRISI', jenjang='KB')
        items = [
            {'nama': 'SISWA A', 'nisn': '111', 'no_telepon': '628111',
             'rombel': kelas_a.nama_kelas},
            {'nama': 'SISWA B', 'nisn': '222', 'no_telepon': '628222',
             'rombel': 'AL JAHIZ'},
        ]
        hasil = _run_import_siswa(items, 'KB')
        self.assertEqual(hasil['dibuat'], 2)
        self.assertEqual(hasil['kelas_dibuat'], ['AL JAHIZ'])
        self.assertEqual(Siswa.objects.get(nik='111').kelas, kelas_a)
        self.assertEqual(Siswa.objects.get(
            nik='222').kelas.nama_kelas, 'AL JAHIZ')

        # import ulang -> update, bukan duplikat
        hasil2 = _run_import_siswa(
            [{'nama': 'SISWA B BARU', 'nisn': '222',
              'no_telepon': '628999', 'rombel': 'AL JAHIZ'}], 'KB')
        self.assertEqual(hasil2['diperbarui'], 1)
        self.assertEqual(hasil2['dibuat'], 0)
        siswa_b = Siswa.objects.get(nik='222')
        self.assertEqual(siswa_b.nama, 'SISWA B BARU')
        self.assertEqual(siswa_b.no_telepon, '628999')
        self.assertEqual(Siswa.objects.count(), 2)

    def test_import_sets_jenjang_of_existing_kelas(self):
        Kelas.objects.create(nama_kelas='AL KINDY', jenjang='KB')
        hasil = _run_import_siswa(
            [{'nama': 'X', 'nisn': '9', 'no_telepon': '-', 'rombel': 'AL KINDY'}], 'TK')
        self.assertEqual(Kelas.objects.get(nama_kelas='AL KINDY').jenjang, 'TK')
        self.assertTrue(hasil['jenjang_diubah'])
