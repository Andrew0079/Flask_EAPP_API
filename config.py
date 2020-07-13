import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'^\x88\xbe\xc5\xdf\x98U\xb3K11\xe1\x12\xab\xebq'"

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }