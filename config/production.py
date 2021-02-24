from config.default import *


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xa5\x17#\x99\x8c\x88\x18\x04(\x08\x83\xd3OX\xaf\xbd'
