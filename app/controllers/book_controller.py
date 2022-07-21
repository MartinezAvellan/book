from typing import Optional, Any
from flask import Blueprint
from app.utils.constants import BOOK_CONTROLLER

blueprint = Blueprint(BOOK_CONTROLLER, __name__)


@blueprint.route('/book-by-title', methods=['POST'])
async def book_by_title() -> Optional[Any]:
    return None


@blueprint.route('/create-book-review-and-rating', methods=['POST'])
async def create_book_review_and_rating() -> Optional[Any]:
    return None


@blueprint.route('/book-details-and-rating', methods=['POST'])
async def book_details_and_rating() -> Optional[Any]:
    return None
