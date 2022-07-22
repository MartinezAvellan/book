from app.services.gutendex_service import get_books_api


class TestGutendexService:

    def test_get_books_api_result_ok(self):
        url: str = 'https://gutendex.com/books/?page=1&ids=84'
        result = get_books_api(url)
        assert result.get('count') == 1

    def test_get_books_api_no_result(self):
        url: str = 'https://gutendex.com/books/?search=aaaaaa'
        result = get_books_api(url)
        assert result.get('count') == 0

    def test_get_books_api_result_error(self):
        url: str = 'https://gutendex.com/books/1/1/'
        result = get_books_api(url)
        assert result.get('results') == []
