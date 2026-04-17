from django.urls import path
from .views import dashboard_view, registrasi_rfid_view, data_kelas_view, data_siswa_view, riwayat_absensi_view, login_view, logout_view, edit_siswa_view, import_siswa_view, absensi_manual_view, kelola_sesi_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('data-kelas/', data_kelas_view, name='data_kelas'),
    path('data-kelas/sesi/<int:kelas_id>/',
         kelola_sesi_view, name='kelola_sesi'),
    path('data-siswa/', data_siswa_view, name='data_siswa'),
    path('data-siswa/edit/<int:id>/', edit_siswa_view, name='edit_siswa'),
    path('data-siswa/import/', import_siswa_view, name='import_siswa'),
    path('absensi-manual/', absensi_manual_view, name='absensi_manual'),
    path('registrasi-rfid/', registrasi_rfid_view, name='registrasi_rfid'),
    path('riwayat-absensi/', riwayat_absensi_view, name='riwayat_absensi'),
]
