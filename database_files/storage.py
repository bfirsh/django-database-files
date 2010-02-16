import base64
from database_files import models
from django.core import files
from django.core.files.storage import Storage
from django.core.urlresolvers import reverse
import os
import StringIO

class DatabaseStorage(Storage):
    def _generate_name(self, name, pk):
        """
        Replaces the filename with the specified pk and removes any dir
        """
        dir_name, file_name = os.path.split(name)
        file_root, file_ext = os.path.splitext(file_name)
        return '%s%s' % (pk, file_ext)
    
    def _open(self, name, mode='rb'):
        try:
            f = models.File.objects.get_from_name(name)
        except models.File.DoesNotExist:
            return None
        fh = StringIO.StringIO(base64.b64decode(f.content))
        fh.name = name
        fh.mode = mode
        fh.size = f.size
        return files.File(fh)
    
    def _save(self, name, content):
        f = models.File.objects.create(
            content=base64.b64encode(content.read()),
            size=content.size,
        )
        return self._generate_name(name, f.pk)
    
    def exists(self, name):
        """
        We generate a new filename for each file, so it will never already 
        exist.
        """
        return False
    
    def delete(self, name):
        try:
            models.File.objects.get_from_name(name).delete()
        except models.File.DoesNotExist:
            pass
    
    def url(self, name):
        return reverse('database_file', kwargs={'name': name})
    
    def size(self, name):
        try:
            return models.File.objects.get_from_name(name).size
        except models.File.DoesNotExist:
            return 0

