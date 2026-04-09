DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'iles_db',
        'USER': 'iles_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT' : '5432',
        
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}