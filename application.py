from flask import Flask

from app.controllers import book_controller
from app.utils.constants import APP_PORT, BASE_URL

application = Flask(__name__)
application.register_blueprint(book_controller.blueprint, url_prefix=BASE_URL)
application.config['JSON_SORT_KEYS'] = False

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=APP_PORT, debug=False)
