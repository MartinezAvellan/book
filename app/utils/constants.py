import os

# APP CONFIG
BASE_URL: str = '/book'
APP_PORT: int = int(os.getenv('APP_PORT', 5000))
ENV: str = os.getenv('ENV', 'PROD')

# DB CONFIG
DB_HOST: str = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT: int = int(os.getenv('DB_PORT', 3306))
DB_USER: str = os.getenv('DB_USER', 'root')
DB_PASSWORD: str = os.getenv('DB_PASSWORD', 'root')
DB_NAME: str = os.getenv('DB_NAME', 'book')
TABLE_REVIEW: str = 'TB_REVIEW'

# REDIS
REDIS_HOST: str = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT: int = int(os.getenv('REDIS_PORT', 6379))
REDIS_TTL: int = int(os.getenv('REDIS_TTL', 300))

# CONTROLLER CONFIG
BOOK_CONTROLLER: str = 'book_controller'

# URL
GUTENDEX_URL: str = 'https://gutendex.com/books/'


# NATIVE QUERIES
NATIVE_QUERY_GET_AVG_RATING_BT_LIMIT: str = 'SELECT book_id, AVG(rating) as rating  FROM TB_REVIEW GROUP BY book_id ORDER BY AVG(rating) DESC LIMIT {};'
NATIVE_QUERY_GET_AVG_RATING_BT_MONTH: str = 'SELECT book_id, AVG(rating) as rating  FROM TB_REVIEW WHERE MONTH(NOW()) = {} GROUP BY book_id ORDER BY AVG(rating) DESC;'
