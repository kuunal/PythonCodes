import os

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('ID')
EMAIL_HOST_PASSWORD = os.environ.get('KEY')
EMAIL_PORT = 587