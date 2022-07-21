from http import HTTPStatus
from flask import Blueprint, request
from app.services.book_service import search_book_by_title
from app.utils.constants import BOOK_CONTROLLER

blueprint = Blueprint(BOOK_CONTROLLER, __name__)


@blueprint.route('/book-by-title/<title>', methods=['GET'])
def book_by_title(title: str):
    books = search_book_by_title(title, request.args.to_dict())
    return books, HTTPStatus.OK


@blueprint.route('/create-book-review-and-rating', methods=['POST'])
def create_book_review_and_rating():
    return None


@blueprint.route('/book-details-and-rating/<id>', methods=['GET'])
def book_details_and_rating(id: int):
    return None
