import calendar
import json
import uuid
from http import HTTPStatus

from flask import Blueprint, request

from app.services.book_service import search_book_by_title, search_book_by_id
from app.services.redis_service import RedisService
from app.services.review_service import ReviewService
from app.utils.constants import BOOK_CONTROLLER, REDIS_TTL
from app.utils.utils import validate_request_body

blueprint = Blueprint(BOOK_CONTROLLER, __name__)
redis_client = RedisService()


@blueprint.route('/book-by-title/<title>', methods=['GET'])
def book_by_title(title: str):
    books: dict
    redis_key: str = title
    args: dict = request.args.to_dict()
    if args.get('page') is not None:
        redis_key = redis_key + '#' + str(args.get('page'))

    books = redis_client.get(redis_key)
    if books is not None:
        return json.loads(books), HTTPStatus.OK

    books = search_book_by_title(title, args)
    redis_client.set(redis_key, json.dumps(books), REDIS_TTL)

    return books, HTTPStatus.OK


@blueprint.route('/create-book-review-and-rating', methods=['POST'])
def create_book_review_and_rating():
    review: dict = request.get_json()
    response = validate_request_body(review)
    if response is not None:
        return response

    result: dict = ReviewService.create_review(review)
    if result is None:
        return {'uuid': uuid.uuid4().__str__(), 'message': 'review cant be created'}, HTTPStatus.BAD_REQUEST

    redis_client.delete(review.get('book_id'))

    return result, HTTPStatus.OK


@blueprint.route('/book-details-and-rating/<book_id>', methods=['GET'])
def book_details_and_rating(book_id: int):
    book: dict
    book = redis_client.get(book_id)
    if book is not None:
        return json.loads(book), HTTPStatus.OK

    book = search_book_by_id(str(book_id))
    if book is None:
        return {'uuid': uuid.uuid4().__str__(), 'message': 'book not found'}, HTTPStatus.BAD_REQUEST

    book['rating'] = 0.0
    book['reviews'] = []
    reviews: dict = ReviewService.get_reviews_and_average(int(book_id))
    if reviews is not None:
        book['rating'] = reviews.get('rating')
        book['reviews'] = reviews.get('reviews')

    redis_client.set(book_id, json.dumps(book), REDIS_TTL)

    return book, HTTPStatus.OK


@blueprint.route('/book-top-number-average-rating/<number>', methods=['GET'])
def book_top_number_average_rating(number: int):
    books = ReviewService.get_average_by_limit(int(number))
    return {"rating top {} avg".format(number): books}, HTTPStatus.OK


@blueprint.route('/book-top-month-average-rating/<month>', methods=['GET'])
def book_top_month_average_rating(month: int):
    books = ReviewService.get_average_by_month(int(month))
    return {"rating top avg by {} ".format(calendar.month_name[int(month)]): books}, HTTPStatus.OK
