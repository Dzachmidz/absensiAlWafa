"""Storage backend media untuk deploy serverless (Vercel).

Filesystem di Vercel read-only -> upload ke media/ gagal dengan Errno 30.
Kelas ini menyimpan file ke Supabase Storage lewat REST API (cukup paket
`requests`, tanpa tambahan dependency boto3).
"""

import posixpath
from urllib.parse import quote

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import Storage


class SupabaseStorage(Storage):
    """Simpan media di Supabase Storage.

    Env yang dibutuhkan:
        SUPABASE_URL          -> https://xxxx.supabase.co
        SUPABASE_SERVICE_KEY  -> service_role key
        SUPABASE_BUCKET       -> nama bucket (default: foto-siswa)
    """

    def __init__(self, **kwargs):
        self.base_url = (
            kwargs.get('base_url')
            or getattr(settings, 'SUPABASE_URL', '')
            or ''
        ).rstrip('/')
        self.service_key = (
            kwargs.get('service_key')
            or getattr(settings, 'SUPABASE_SERVICE_KEY', '')
            or ''
        )
        self.bucket = (
            kwargs.get('bucket')
            or getattr(settings, 'SUPABASE_BUCKET', '')
            or 'foto-siswa'
        )

    # ---------- helpers ----------
    def _clean(self, name):
        return posixpath.normpath(str(name)).lstrip('/')

    def _object_url(self, name):
        return f'{self.base_url}/storage/v1/object/{self.bucket}/{self._clean(name)}'

    def _headers(self, extra=None):
        # `apikey` wajib untuk key model baru Supabase (sb_secret_...),
        # dan aman juga untuk legacy service_role JWT.
        headers = {
            'Authorization': f'Bearer {self.service_key}',
            'apikey': self.service_key,
        }
        if extra:
            headers.update(extra)
        return headers

    # ---------- Django Storage API ----------
    def url(self, name):
        return (f'{self.base_url}/storage/v1/object/public/'
                f'{self.bucket}/{quote(self._clean(name))}')

    def _save(self, name, content):
        content.seek(0)
        payload = content.read()
        mime = getattr(content, 'content_type', None) or 'application/octet-stream'

        response = requests.post(
            self._object_url(name),
            data=payload,
            headers=self._headers({
                'Content-Type': mime,
                'x-upsert': 'true',
                'cache-control': '3600',
            }),
            timeout=60,
        )
        if response.status_code >= 300:
            raise IOError(
                f'Supabase Storage gagal upload ({response.status_code}): '
                f'{response.text[:200]}'
            )
        return name

    def _open(self, name, mode='rb'):
        response = requests.get(self._object_url(name),
                                headers=self._headers(), timeout=60)
        if response.status_code >= 300:
            raise IOError(f'File tidak ditemukan di Supabase Storage: {name}')
        return ContentFile(response.content, name=self._clean(name))

    def exists(self, name):
        try:
            response = requests.head(self._object_url(name),
                                     headers=self._headers(), timeout=15)
            return response.status_code < 400
        except requests.RequestException:
            return False

    def delete(self, name):
        try:
            requests.delete(self._object_url(name),
                            headers=self._headers(), timeout=30)
        except requests.RequestException:
            pass

    def size(self, name):
        response = requests.head(self._object_url(name),
                                 headers=self._headers(), timeout=15)
        return int(response.headers.get('content-length', 0) or 0)


def using_supabase():
    return (getattr(settings, 'STORAGES', {})
            .get('default', {})
            .get('BACKEND', '')
            .endswith('SupabaseStorage'))
