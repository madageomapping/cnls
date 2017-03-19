DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'onusida', # Name of your spatial database
        'USER': 'onusida', # Database user
        'PASSWORD': 'onusida', # Database password 
        'HOST': 'postgis',
        'PORT':'5432',
    }
}

# A adapter selon les installations
GEOS_LIBRARY_PATH = '/usr/local/lib/libgeos_c.so'
