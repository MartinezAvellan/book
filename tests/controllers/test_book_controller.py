import json
from http import HTTPStatus

import pytest
from pytest_mock import MockerFixture

from app.controllers.book_controller import book_by_title, create_book_review_and_rating, \
    book_top_number_average_rating, book_top_month_average_rating, book_details_and_rating
from application import application


class TestBookController:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.title = 'aaaaaa'
        self.number = 5
        self.book_id = 84
        self.content_type = 'application/json'

    def test_book_by_title(self, mocker: MockerFixture):
        with application.test_request_context('url', headers={}, query_string={'page': 1}):
            mock_response = self.get_book_by_title()
            mock = mocker.patch('app.controllers.book_controller.redis_client.get', return_value=None)
            mock_1 = mocker.patch('app.controllers.book_controller.search_book_by_title', return_value=mock_response)
            mock_2 = mocker.patch('app.controllers.book_controller.redis_client.set', return_value=None)
            result, status = book_by_title(self.title)
            assert result is not None
            assert status == HTTPStatus.OK
            mock.assert_called_once()
            mock_1.assert_called_once()
            mock_2.assert_called_once()

    def test_book_by_title_by_redis(self, mocker: MockerFixture):
        with application.test_request_context('url', headers={}):
            mock_response = json.dumps(self.get_book_by_title())
            mock = mocker.patch('app.controllers.book_controller.redis_client.get', return_value=mock_response)
            result, status = book_by_title(self.title)
            assert result is not None
            assert status == HTTPStatus.OK
            mock.assert_called_once()

    def test_create_book_review_and_rating_validate_body(self):
        request = json.dumps(self.get_book_review_is_not_none())
        with application.test_request_context('url', headers={}, data=request, content_type=self.content_type):
            result, status = create_book_review_and_rating()
            assert result is not None
            assert status == HTTPStatus.BAD_REQUEST

    def test_create_book_review_and_rating_not_create_review(self, mocker: MockerFixture):
        request = json.dumps(self.get_book_review())
        with application.test_request_context('url', headers={}, data=request, content_type=self.content_type):
            mock = mocker.patch('app.controllers.book_controller.ReviewService.create_review', return_value=None)
            result, status = create_book_review_and_rating()
            assert result is not None
            assert status == HTTPStatus.BAD_REQUEST
            mock.assert_called_once()

    def test_create_book_review_and_rating(self, mocker: MockerFixture):
        request = json.dumps(self.get_book_review())
        with application.test_request_context('url', headers={}, data=request, content_type=self.content_type):
            mock = mocker.patch('app.controllers.book_controller.ReviewService.create_review',
                                return_value=self.get_book_review_db())
            mock_1 = mocker.patch('app.controllers.book_controller.redis_client.delete', return_value=None)
            result, status = create_book_review_and_rating()
            assert result is not None
            assert status == HTTPStatus.OK
            mock.assert_called_once()
            mock_1.assert_called_once()

    def test_book_top_number_average_rating(self, mocker: MockerFixture):
        with application.test_request_context('url', headers={}):
            mock = mocker.patch('app.controllers.book_controller.ReviewService.get_average_by_limit',
                                return_value=self.book_average_rating())
            result, status = book_top_number_average_rating(self.number)
            assert result is not None
            assert status == HTTPStatus.OK
            mock.assert_called_once()

    def test_book_top_month_average_rating(self, mocker: MockerFixture):
        with application.test_request_context('url', headers={}):
            mock = mocker.patch('app.controllers.book_controller.ReviewService.get_average_by_month',
                                return_value=self.book_average_rating())
            result, status = book_top_month_average_rating(self.number)
            assert result is not None
            assert status == HTTPStatus.OK
            mock.assert_called_once()

    def test_book_details_and_rating_by_redis(self, mocker: MockerFixture):
        with application.test_request_context('url', headers={}):
            mock_response = json.dumps(self.get_book_by_title())
            mock = mocker.patch('app.controllers.book_controller.redis_client.get', return_value=mock_response)
            result, status = book_details_and_rating(self.book_id)
            assert result is not None
            assert status == HTTPStatus.OK
            mock.assert_called_once()

    def test_book_details_and_rating_by_redis_by_db(self, mocker: MockerFixture):
        with application.test_request_context('url', headers={}):
            mock = mocker.patch('app.controllers.book_controller.redis_client.get', return_value=None)
            mock_1 = mocker.patch('app.controllers.book_controller.search_book_by_id', return_value=None)
            result, status = book_details_and_rating(self.book_id)
            assert result is not None
            assert status == HTTPStatus.BAD_REQUEST
            mock.assert_called_once()
            mock_1.assert_called_once()

    def test_book_details_and_rating(self, mocker: MockerFixture):
        with application.test_request_context('url', headers={}):
            mock_response = self.get_book_by_title()
            mock_response_reviews = self.get_book_reviews()
            mock = mocker.patch('app.controllers.book_controller.redis_client.get', return_value=None)
            mock_1 = mocker.patch('app.controllers.book_controller.search_book_by_id', return_value=mock_response)
            mock_2 = mocker.patch('app.controllers.book_controller.ReviewService.get_reviews_and_average',
                                  return_value=mock_response_reviews)
            mock_3 = mocker.patch('app.controllers.book_controller.redis_client.set', return_value=None)
            result, status = book_details_and_rating(self.book_id)
            assert result is not None
            assert status == HTTPStatus.OK
            mock.assert_called_once()
            mock_1.assert_called_once()
            mock_2.assert_called_once()
            mock_3.assert_called_once()

    @staticmethod
    def get_book_reviews():
        return {
            "book_id": 84,
            "rating": 3.7,
            "reviews": [
                "Este livro eh mais ou menos...2",
                "Este livro eh mais ou menos...1",
                "Este livro eh bom demais 5",
                "Este livro eh bom 4",
                "Este livro eh medio 3",
                "Este livro eh medio 3",
                "Este livro eh medio 3",
                "Este livro eh medio 3",
                "Este livro eh medio 3"
            ]
        }

    @staticmethod
    def get_book_review():
        return {
            "book_id": 84,
            "rating": 2,
            "review": "Este livro eh medio 2"
        }

    @staticmethod
    def get_book_review_db():
        return {
            "id": 1,
            "book_id": 84,
            "rating": 2,
            "review": "Este livro eh medio 2"
        }

    @staticmethod
    def get_book_review_is_not_none():
        return {
            "rating": 2,
            "review": "Este livro eh medio 2"
        }

    @staticmethod
    def get_book_by_title():
        return {
            "next": None,
            "previous": None,
            "books": [{
                "id": 84,
                "title": "Frankenstein; Or, The Modern Prometheus",
                "authors": [
                    {
                        "name": "Shelley, Mary Wollstonecraft",
                        "birth_year": 1797,
                        "death_year": 1851
                    }
                ],
                "languages": [
                    "en"
                ],
                "download_count": 17482
            }]
        }

    @staticmethod
    def book_average_rating():
        return {
            "message": "rating top avg by July",
            "ratings": [
                {
                    "book_id": 1,
                    "rating": 5.0
                },
                {
                    "book_id": 2,
                    "rating": 4.0
                },
                {
                    "book_id": 84,
                    "rating": 3.0
                },
                {
                    "book_id": 4,
                    "rating": 1.7
                },
                {
                    "book_id": 3,
                    "rating": 1.5
                }
            ]}
