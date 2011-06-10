django-database-files
=====================

django-database-files is a storage system for Django that stores uploaded files 
in the database.

WARNING: It is generally a bad idea to serve static files from Django, 
but there are some valid use cases. If your Django app is behind a caching 
reverse proxy and you need to scale your application servers, it may be 
simpler to store files in the database.

Requires:

  * Django 1.1

Installation
------------

    $ python setup.py install

Usage
-----

In ``settings.py``, add ``database_files`` to your ``INSTALLED_APPS`` and add this line:

    DEFAULT_FILE_STORAGE = 'database_files.storage.DatabaseStorage'

Although ``upload_to`` is a required argument on ``FileField``, it is not used for 
storing files in the database. Just set it to a dummy value:

    upload = models.FileField(upload_to='not required')

All your ``FileField`` and ``ImageField`` files will now be stored in the 
database.

Test suite
----------

    $ ./run_tests.sh

