
from south.db import db
from django.db import models
from database_files.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'File'
        db.create_table('database_files_file', (
            ('id', orm['database_files.File:id']),
            ('content', orm['database_files.File:content']),
            ('size', orm['database_files.File:size']),
        ))
        db.send_create_signal('database_files', ['File'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'File'
        db.delete_table('database_files_file')
        
    
    
    models = {
        'database_files.file': {
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        }
    }
    
    complete_apps = ['database_files']
