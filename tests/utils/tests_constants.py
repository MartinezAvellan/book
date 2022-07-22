from pytest_mock import MockerFixture

from app.utils.constants import *


def test_constants():
    assert BASE_URL == '/book'
    assert APP_PORT == 5000
    assert ENV == 'PROD'
    assert DB_HOST == '127.0.0.1'
    assert DB_PORT == 3306
    assert DB_USER == 'root'
    assert DB_PASSWORD == 'root'
    assert DB_NAME == 'book'
    assert TABLE_REVIEW == 'TB_REVIEW'
    assert REDIS_HOST == '127.0.0.1'
    assert REDIS_PORT == 6379
    assert REDIS_TTL == 300
    assert BOOK_CONTROLLER == 'book_controller'
    assert GUTENDEX_URL == 'https://gutendex.com/books/'
    assert NATIVE_QUERY_GET_AVG_RATING_BT_LIMIT == 'SELECT book_id, AVG(rating) as rating  FROM TB_REVIEW GROUP BY book_id ORDER BY AVG(rating) DESC LIMIT {};'
    assert NATIVE_QUERY_GET_AVG_RATING_BT_MONTH == 'SELECT book_id, AVG(rating) as rating  FROM TB_REVIEW WHERE MONTH(NOW()) = {} GROUP BY book_id ORDER BY AVG(rating) DESC;'
