from django.core import files
from django.test import TestCase
from database_files.models import File
from database_files.tests.models import Thing
import StringIO

class DatabaseFilesTestCase(TestCase):
    def test_adding_file(self):
        test_file = files.temp.NamedTemporaryFile(
            suffix='.txt',
            dir=files.temp.gettempdir()
        )
        test_file.write('1234567890')
        test_file.seek(0)
        t = Thing.objects.create(
            upload=files.File(test_file),
        )
        self.assertEqual(File.objects.count(), 1)
        t = Thing.objects.get(pk=t.pk)
        self.assertEqual(t.upload.file.size, 10)
        self.assertEqual(t.upload.file.name[-4:], '.txt')
        self.assertEqual(t.upload.file.read(), '1234567890')
        t.upload.delete()
        self.assertEqual(File.objects.count(), 0)

class DatabaseFilesViewTestCase(TestCase):
    fixtures = ['test_data.json']
    
    def test_reading_file(self):
        response = self.client.get('/1.txt')
        self.assertEqual(response.content, '1234567890')
        self.assertEqual(response['content-type'], 'text/plain')
        self.assertEqual(unicode(response['content-length']), '10')

