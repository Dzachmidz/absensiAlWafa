"""Cek konfigurasi penyimpanan media (Supabase Storage) sebelum deploy.

    python manage.py check_media_storage
"""

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

from absensi.storage import using_supabase

PROBE_NAME = 'foto_siswa/_tes_storage.txt'


class Command(BaseCommand):
    help = 'Uji upload/hapus/buka file di storage media yang aktif'

    def handle(self, *args, **options):
        ok = True
        backend = settings.STORAGES.get('default', {}).get('BACKEND', '-')

        self.stdout.write(f'Backend media : {backend}')
        self.stdout.write(f'SUPABASE_URL  : {getattr(settings, "SUPABASE_URL", "") or "-"}')
        self.stdout.write(f'Bucket        : {getattr(settings, "SUPABASE_BUCKET", "") or "-"}')

        key = getattr(settings, 'SUPABASE_SERVICE_KEY', '') or ''
        if key:
            self.stdout.write(f'Key           : {key[:12]}... ({len(key)} karakter)')
        else:
            self.stdout.write(self.style.WARNING('Key           : KOSONG'))

        if not using_supabase():
            self.stdout.write(self.style.WARNING(
                '\nStorage masih lokal (bukan Supabase). Di server/Vercel, set '
                'SUPABASE_SERVICE_KEY (dan SUPABASE_URL kalau bukan dari DATABASE_URL).'))
            return

        # 1. upload
        try:
            name = default_storage.save(PROBE_NAME, ContentFile(b'ping'))
            self.stdout.write(self.style.SUCCESS(f'upload  : OK ({name})'))
        except Exception as exc:                            # noqa: BLE001
            ok = False
            self.stdout.write(self.style.ERROR(f'upload  : GAGAL -> {exc}'))
            self.stdout.write(
                '\nKemungkinan penyebab: bucket belum dibuat, bucket tidak public, '
                'atau key salah (pakai Secret key / service_role, bukan publishable/anon).')
            return

        # 2. url publik
        url = default_storage.url(name)
        self.stdout.write(f'url     : {url}')

        # 3. buka lagi
        try:
            with default_storage.open(name, 'rb') as handle:
                self.stdout.write(self.style.SUCCESS(
                    f'read    : OK ({handle.read()[:16]!r})'))
        except Exception as exc:                            # noqa: BLE001
            ok = False
            self.stdout.write(self.style.ERROR(f'read    : GAGAL -> {exc}'))

        # 4. hapus file uji
        try:
            default_storage.delete(name)
            self.stdout.write(self.style.SUCCESS('delete  : OK'))
        except Exception as exc:                            # noqa: BLE001
            ok = False
            self.stdout.write(self.style.ERROR(f'delete  : GAGAL -> {exc}'))

        self.stdout.write('')
        if ok:
            self.stdout.write(self.style.SUCCESS('Storage media siap dipakai.'))
        else:
            self.stdout.write(self.style.ERROR('Storage media belum siap.'))
