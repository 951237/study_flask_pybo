from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views   # views 하위폴더의 main_views파일 호출
    app.register_blueprint(main_views.bp)

    return app

