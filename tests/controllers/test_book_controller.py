import json
from http import HTTPStatus

import pytest
from pytest_mock import MockerFixture

from app.controllers.book_controller import book_by_title
from application import application


class TestBookController:

    @pytest.fixture(autouse=True)
    def setup(self, mocker: MockerFixture):
        self.title = 'aaaaaa'

    def test_book_by_title(self, mocker: MockerFixture):
        with application.test_request_context('url', headers={}):
            mock_response = self.get_book_by_title()

            mock = mocker.patch('app.controllers.v1.book_controller.redis_client.get', return_value=None)
            mock_2 = mocker.patch('app.controllers.v1.book_controller.redis_client.get', return_value=mock_response)

            result, status = book_by_title(self.title)
            data = json.loads(result.get_data())
            assert data is not None
            assert status == HTTPStatus.OK

            mock.assert_called_once()
            mock_2.assert_called_once()

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
