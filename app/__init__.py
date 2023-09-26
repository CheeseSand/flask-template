from flask import Flask

def create_app():
    app = Flask(__name__)

    # 여기에 애플리케이션 설정 및 확장 기능을 추가할 수 있음

    from . import errors, index, test
    app.register_blueprint(errors.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(test.bp)

    return app
