import os

# APP CONFIG
BASE_URL = '/book'
APP_PORT = os.getenv('APP_PORT', 5000)
ENV = os.getenv('ENV', 'PROD')

# DB CONFIG
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('DB_PORT', 3306)
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
DB_NAME = os.getenv('DB_NAME', 'book')
TABLE_REVIEW = 'TB_REVIEW'

# CONTROLLER CONFIG
BOOK_CONTROLLER = 'book_controller'

# URL
GUTENDEX_URL = 'https://gutendex.com/books/'
