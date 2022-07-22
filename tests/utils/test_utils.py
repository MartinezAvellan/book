from http import HTTPStatus

from app.utils.utils import find_number_of_page, validate_request_body


class TestUtils:

    def test_find_number_of_page(self):
        value = 1
        result = find_number_of_page('https:/localhost:5000/books/?page=1&search=Frankenstein')
        assert value == result

    def test_validate_request_body_book_id_is_required(self):
        body = {
            "rating": 2,
            "review": "Este livro eh medio 2"
        }
        message, http_status = validate_request_body(body)
        assert 'book_id is required' == message.get('message')
        assert HTTPStatus.BAD_REQUEST == http_status

    def test_validate_request_body_book_id_is_not_int(self):
        body = {
            "book_id": "84",
            "rating": 2,
            "review": "Este livro eh medio 2"
        }
        message, http_status = validate_request_body(body)
        assert 'book_id is not integer' == message.get('message')
        assert HTTPStatus.BAD_REQUEST == http_status

    def test_validate_request_body_review_is_required(self):
        body = {
            "book_id": 85,
            "rating": 2
        }
        message, http_status = validate_request_body(body)
        assert 'review is required' == message.get('message')
        assert HTTPStatus.BAD_REQUEST == http_status

    def test_validate_request_body_review_is_not_string(self):
        body = {
            "book_id": 85,
            "rating": 2,
            "review": 22222
        }
        message, http_status = validate_request_body(body)
        assert 'review is not string' == message.get('message')
        assert HTTPStatus.BAD_REQUEST == http_status

    def test_validate_request_body_review_is_not_length(self):
        body = {
            "book_id": 85,
            "rating": 2,
            "review": ""
        }
        message, http_status = validate_request_body(body)
        assert 'review must be between 0-250 characters' == message.get('message')
        assert HTTPStatus.BAD_REQUEST == http_status

    def test_validate_request_body_rating_is_required(self):
        body = {
            "book_id": 85,
            "review": "asdasdsadadd"
        }
        message, http_status = validate_request_body(body)
        assert 'rating is required' == message.get('message')
        assert HTTPStatus.BAD_REQUEST == http_status

    def test_validate_request_body_rating_is_not_int(self):
        body = {
            "book_id": 84,
            "rating": "2",
            "review": "Este livro eh medio 2"
        }
        message, http_status = validate_request_body(body)
        assert 'rating is not valid integer' == message.get('message')
        assert HTTPStatus.BAD_REQUEST == http_status

    def test_validate_request_body_rating_is_not_range(self):
        body = {
            "book_id": 84,
            "rating": 6,
            "review": "Este livro eh medio 2"
        }
        message, http_status = validate_request_body(body)
        assert 'rating is not a range valid between 0-5' == message.get('message')
        assert HTTPStatus.BAD_REQUEST == http_status

    def test_validate_request_body_else(self):
        body = {
            "book_id": 84,
            "rating": 5,
            "review": "Este livro eh medio 2"
        }
        message = validate_request_body(body)
        assert message is None
