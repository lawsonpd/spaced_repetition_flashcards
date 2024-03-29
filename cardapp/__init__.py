import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='f5347f004eb706c4cadbb1f275131593db2fea3f22c02b4dfedf3427c8542fc7',
        DATABASE=os.path.join(app.instance_path, 'cardapp.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple home page placeholder
    @app.route('/')
    def main():
        return render_template('main.html')

    from . import db
    db.init_app(app)

    from . import cardsets
    app.register_blueprint(cardsets.bp)
    # app.add_url_rule('/', endpoint='cardsets.index')

    from . import cards
    app.register_blueprint(cards.bp)

    return app
