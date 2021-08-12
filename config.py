import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URL = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # 데이터베이스 접속주소
SQLALCHEMY_TRACK_MODIFICATIONS = False # sqlalchemy 이벤트 처리 옵션

