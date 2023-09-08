# from flask import Flask
# app = Flask(__name__)  #플라스크 애플리케이션 생성하는 코드, __name__이라는 변수에는 모듈명이 담긴다
# # 즉, 이 파일이 실행되면 pybo.py 라는 모듈이 실행되는 것이므로 __name__변수에는 "pybo" 라는 문자열이 담긴다.
# # @app.route 는 URL과 플라스크 코드를 매핑하는 플라스크의 데코레이터다. 즉, / URL이 요청되면 플라스크는 hello_pybo 함수를 실행시킨다.
#
#
# @app.route('/')
# def hello_pybo():
#     return 'Hello, Pybo!'  #Hello pybo! 를 출력

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flaskext.markdown import Markdown

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    return app