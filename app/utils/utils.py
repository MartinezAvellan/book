import uuid
from http import HTTPStatus


def find_number_of_page(url: str) -> int:
    page: int = None
    if url is not None and 'page=' in url:
        start = url.find("?page=") + len("?page=")
        end = url.find("&")
        page = int(url[start:end])

    return page


def validate_request_body(body: dict) -> dict:
    uuid_str = uuid.uuid4().__str__()
    if body.get('book_id') is None:
        return {'uuid': uuid_str, 'message': 'book_id is required'}, HTTPStatus.BAD_REQUEST
    elif not isinstance(body.get('book_id'), int):
        return {'uuid': uuid_str, 'message': 'book_id is not integer'}, HTTPStatus.BAD_REQUEST
    elif body.get('review') is None:
        return {'uuid': uuid_str, 'message': 'review is required'}, HTTPStatus.BAD_REQUEST
    elif not isinstance(body.get('review'), str):
        return {'uuid': uuid_str, 'message': 'review is not string'}, HTTPStatus.BAD_REQUEST
    elif len(body.get('review')) < 1 or len(body.get('review')) > 250:
        return {'uuid': uuid_str, 'message': 'review must be between 0-100 characters'}, HTTPStatus.BAD_REQUEST
    elif body.get('rating') is None:
        return {'uuid': uuid_str, 'message': 'rating is required'}, HTTPStatus.BAD_REQUEST
    elif not isinstance(body.get('rating'), int):
        return {'uuid': uuid_str, 'message': 'rating is not valid integer'}, HTTPStatus.BAD_REQUEST
    elif body.get('rating') < 0 or body.get('rating') > 5:
        return {'uuid': uuid_str, 'message': 'rating is not a range valid between 0-5'}, HTTPStatus.BAD_REQUEST
    else:
        None
