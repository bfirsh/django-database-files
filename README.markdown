django-database-files
=====================

django-database-files is a storage system for Django that stores uploaded files 
in the database.

BIG SCARY WARNING: It is generally a bad idea to serve static files from Django, 
but there are some valid use cases. If your Django app is behind a caching 
reverse proxy and you need to scale your application servers, it may be 
simpler to store files in the database instead of using a distributed 
filesystem.

Requires:

  * Django 1.1

Installation
------------

    $ python setup.py install

Usage
-----

In ``settings.py``, add ``'database_files'`` to your INSTALLED_APPS and add this line:

    DEFAULT_FILE_STORAGE = 'database_files.storage.DatabaseStorage'

Although the ``upload_to`` argument on ``FileField`` is required, it is not 
used by ``database_files``. Just set it to a dummy value:

    upload = models.FileField(upload_to='not required')

All your ``FileField`` and ``ImageField`` files will now be stored in the 
database.

