from unittest import mock

from django.core.files.base import ContentFile
from django.test import SimpleTestCase, override_settings

from absensi.storage import SupabaseStorage, using_supabase


@override_settings(
    SUPABASE_URL='https://demo.supabase.co',
    SUPABASE_SERVICE_KEY='service-key',
    SUPABASE_BUCKET='foto-siswa',
    STORAGES={'default': {'BACKEND': 'absensi.storage.SupabaseStorage'}},
)
class SupabaseStorageTest(SimpleTestCase):
    def setUp(self):
        self.storage = SupabaseStorage()

    def test_using_supabase_detects_backend(self):
        self.assertTrue(using_supabase())

    def test_url_is_public_object_url(self):
        self.assertEqual(
            self.storage.url('foto_siswa/123.png'),
            'https://demo.supabase.co/storage/v1/object/public/foto-siswa/foto_siswa/123.png',
        )

    @mock.patch('absensi.storage.requests.post')
    def test_save_uploads_bytes_with_service_key(self, post):
        post.return_value = mock.Mock(status_code=200, text='ok')
        content = ContentFile(b'abc', name='x.png')
        content.content_type = 'image/png'

        name = self.storage.save('foto_siswa/x.png', content)

        self.assertEqual(name, 'foto_siswa/x.png')
        args, kwargs = post.call_args
        self.assertTrue(args[0].endswith('/storage/v1/object/foto-siswa/foto_siswa/x.png'))
        self.assertEqual(kwargs['data'], b'abc')
        self.assertEqual(kwargs['headers']['Authorization'], 'Bearer service-key')
        self.assertEqual(kwargs['headers']['apikey'], 'service-key')
        self.assertEqual(kwargs['headers']['Content-Type'], 'image/png')
        self.assertEqual(kwargs['headers']['x-upsert'], 'true')

    @mock.patch('absensi.storage.requests.post')
    def test_save_raises_ioerror_on_failure(self, post):
        post.return_value = mock.Mock(status_code=403, text='bucket not found')
        content = ContentFile(b'abc', name='x.png')
        with self.assertRaises(IOError) as ctx:
            self.storage.save('x.png', content)
        self.assertIn('403', str(ctx.exception))

    @mock.patch('absensi.storage.requests.head')
    def test_exists(self, head):
        head.return_value = mock.Mock(status_code=200)
        self.assertTrue(self.storage.exists('a.png'))
        head.return_value = mock.Mock(status_code=404)
        self.assertFalse(self.storage.exists('a.png'))

    @mock.patch('absensi.storage.requests.get')
    def test_open_returns_content(self, get):
        get.return_value = mock.Mock(status_code=200, content=b'img')
        self.assertEqual(self.storage.open('a.png').read(), b'img')


@override_settings(SUPABASE_URL='', SUPABASE_SERVICE_KEY='',
                   STORAGES={'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'}})
class LocalStorageTest(SimpleTestCase):
    def test_using_supabase_false_on_local(self):
        self.assertFalse(using_supabase())
