"""
Django settings for haiku project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Application definition


INSTALLED_APPS = (
    'django_admin_bootstrapped',
    #default apps#####################
    #'django.contrib.admin.apps.AdminConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ##################################
    'haiku.apps.admin',
    'haiku.apps.geo',
    'haiku.apps.people',
    'haiku.apps.texts',
    'south',
    'import_export',
    'adminsortable',
    # uncomment in your greatest time of need!
    #NOTE: as of 8/12/2014 the pypi version does not support Natural Keys
    # This version does: https://github.com/athom09/django-fixture-magic
    # Hopefully one day the guy will pull my PullRequest
    #'fixture_magic',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # Default processors##############################
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    ##################################################
    "django.core.context_processors.request",
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ROOT_URLCONF = 'haiku.urls'

WSGI_APPLICATION = 'haiku.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# STATICFILES_DIRS = ( os.path.join('static'), )

STATIC_URL = '/static/'
STATIC_ROOT = 'static'



TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_DIR = 'test-results'


# disable south tests and migrations when running tests
# - without these settings, test fail on loading initial fixtured data
SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False

# used with admin_reorder template tag
ADMIN_REORDER = (
    ("texts", ('Kigo', 'Verse', 'Work')),
    ("people", ('Person', 'School')),
    ("geo", ('Structure', 'City', 'Province','Area', 'ModernCity', 'ModernPrefecture', 'ModernArea')),
    ("auth", ('User', 'Group',)),
)

import sys

# import localsettings
# This will override any previously set value
try:
    from localsettings import *
except ImportError:
    print >>sys.stderr, '''Settings not defined. Please configure a version
        of localsettings.py for this site. See localsettings.py.dist for
        setup details.'''

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'
