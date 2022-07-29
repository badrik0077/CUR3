import logging

from flask import Flask

from app.views import post_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# logging.basicConfig(filename='basic.log', level=logging.INFO)


app.register_blueprint(post_blueprint)


if __name__ == '__main__':
    app.run()
