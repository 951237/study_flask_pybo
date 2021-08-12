from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy     # DB ORM 라이브러리

import config   # 설정파일 불러오기

db = SQLAlchemy()   # 데이터베이스 생성
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)  #app.config 환경 변수로 부르기

    #ORM 
    db.init_app(app)    # 초기화
    migrate.init_app(app, db)

    from . import models    # 모델 가져오기 

    from .views import main_views   # views 하위폴더의 main_views파일 호출
    app.register_blueprint(main_views.bp)

    # 블루프린트 객체 등록
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    
    return app

