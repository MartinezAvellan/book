import uuid
from http import HTTPStatus
from flask import Blueprint, request
from app.services.book_service import search_book_by_title, search_book_by_id
from app.services.review_service import ReviewService
from app.utils.constants import BOOK_CONTROLLER
from app.utils.utils import validate_request_body

blueprint = Blueprint(BOOK_CONTROLLER, __name__)


@blueprint.route('/book-by-title/<title>', methods=['GET'])
def book_by_title(title: str):
    books = search_book_by_title(title, request.args.to_dict())

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

    return result, HTTPStatus.OK


@blueprint.route('/book-details-and-rating/<book_id>', methods=['GET'])
def book_details_and_rating(book_id: int):
    book: dict = search_book_by_id(book_id)
    if book is None:
        return {'uuid': uuid.uuid4().__str__(), 'message': 'book not found'}, HTTPStatus.BAD_REQUEST

    reviews: dict = ReviewService.get_reviews_and_average(book_id)
    book['rating'] = reviews.get('rating')
    book['reviews'] = reviews.get('reviews')

    return book, HTTPStatus.OK
