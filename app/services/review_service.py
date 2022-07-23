from typing import Any

from peewee import Database
from app.models.review import Review
from app.repository.base_model import BaseModel
from app.utils.constants import NATIVE_QUERY_GET_AVG_RATING_BT_LIMIT, NATIVE_QUERY_GET_AVG_RATING_BT_MONTH

db: Database = BaseModel.get_database()


class ReviewService:

    @staticmethod
    def create_review(review: dict) -> Any:
        try:
            review = Review.create(
                book_id=review.get('book_id'),
                rating=review.get('rating'),
                review=review.get('review'),
            )
            book_review: dict = {
                'id': review.id,
                'book_id': review.book_id,
                'rating': review.rating,
                'review': review.review,
            }
            return book_review
        except Exception as e:
            print({'Error: ': 'review cant be created', 'book_id': review.get('book_id'), 'exception': e.args})
            return None

    @staticmethod
    def get_reviews_and_average(book_id: int) -> Any:
        try:
            reviews = []
            sum_ratings: int = 0
            result = Review.select().where(Review.book_id == book_id).order_by(Review.id)
            for review in result:
                reviews.append(review.review)
                sum_ratings = sum_ratings + int(review.rating)

            rating: float = sum_ratings / len(result)
            return {
                'book_id': book_id,
                'rating': round(rating, 1),
                'reviews': reviews
            }
        except Exception as e:
            print({'Error: ': e.args})
            return None

    @staticmethod
    def get_average_by_limit(number: int) -> Any:
        try:
            books = []
            cursor = db.execute_sql(NATIVE_QUERY_GET_AVG_RATING_BT_LIMIT.format(int(number)))
            for review in cursor.fetchall():
                books.append({
                    'book_id': review[0],
                    'rating': round(review[1], 1),
                })

            return books
        except Exception as e:
            print({'Error: ': e.args})
            return None

    @staticmethod
    def get_average_by_month(month: int) -> Any:
        try:
            books = []
            cursor = db.execute_sql(NATIVE_QUERY_GET_AVG_RATING_BT_MONTH.format(int(month)))
            for review in cursor.fetchall():
                books.append({
                    'book_id': review[0],
                    'rating': round(review[1], 1),
                })

            return books
        except Exception as e:
            print({'Error: ': e.args})
            return None
