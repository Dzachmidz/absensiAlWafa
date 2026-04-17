from django.contrib import admin
from .models import Siswa, Absensi


@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nik', 'kelas', 'no_telepon',
                    'rfid_uid', 'created_at')
    search_fields = ('nama', 'nik', 'rfid_uid', 'kelas')
    list_filter = ('kelas', 'created_at')
    ordering = ('nama',)


@admin.register(Absensi)
class AbsensiAdmin(admin.ModelAdmin):
    list_display = ('siswa', 'hari', 'tanggal', 'jam_masuk', 'jam_keluar')
    list_filter = ('tanggal', 'hari', 'siswa__kelas')
    search_fields = ('siswa__nama', 'siswa__nik')
    date_hierarchy = 'tanggal'
    ordering = ('-tanggal', '-jam_masuk')
