"""Upload semua file media lokal ke storage aktif (mis. Supabase Storage).

Dipakai sekali setelah pindah storage supaya foto lama tetap tampil:

    python manage.py sync_media_supabase
"""

import os

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Upload file di MEDIA_ROOT ke storage default (mis. Supabase Storage)'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true',
                            help='Hanya tampilkan file yang akan diupload')

    def handle(self, *args, **options):
        media_root = str(settings.MEDIA_ROOT)
        if not os.path.isdir(media_root):
            self.stdout.write(self.style.WARNING(
                f'Folder media tidak ada: {media_root}'))
            return

        uploaded = skipped = failed = 0

        for root, _dirs, files in os.walk(media_root):
            for filename in files:
                if filename.startswith('.'):
                    continue
                full_path = os.path.join(root, filename)
                name = os.path.relpath(full_path, media_root).replace(os.sep, '/')

                if default_storage.exists(name):
                    skipped += 1
                    continue

                if options['dry_run']:
                    self.stdout.write(f'[dry-run] {name}')
                    continue

                try:
                    with open(full_path, 'rb') as handle:
                        default_storage.save(name, handle)
                    uploaded += 1
                    self.stdout.write(f'uploaded: {name}')
                except Exception as exc:                     # noqa: BLE001
                    failed += 1
                    self.stderr.write(f'gagal: {name} -> {exc}')

        self.stdout.write(self.style.SUCCESS(
            f'Selesai. uploaded={uploaded} skipped={skipped} failed={failed}'))
