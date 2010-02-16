from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<name>.+)$', 'database_files.views.serve', name='database_file'),
)
