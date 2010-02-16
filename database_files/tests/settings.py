DATABASE_ENGINE = 'sqlite3'
ROOT_URLCONF = 'database_files.urls'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'database_files',
    'database_files.tests',
]
DEFAULT_FILE_STORAGE = 'database_files.storage.DatabaseStorage'
