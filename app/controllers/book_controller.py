from http import HTTPStatus
from flask import Blueprint, request
from app.services.book_service import search_book_by_title
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
    return result, HTTPStatus.OK


@blueprint.route('/book-details-and-rating/<id>', methods=['GET'])
def book_details_and_rating(id: int):
    return None
