from django.db import models
from database_files.manager import FileManager

class File(models.Model):
    content = models.TextField()
    size = models.IntegerField()
    
    objects = FileManager()

