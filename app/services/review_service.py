import datetime
from typing import Any

from peewee import fn
from app.models.review import Review


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
            raise None

    @staticmethod
    def get_average_by_limit(number: int) -> list:
        try:
            books = []
            response = (Review.select(Review.book_id, fn.AVG(Review.rating).alias('avg_rating'))
                        .group_by(Review.book_id)
                        .order_by(fn.AVG(Review.rating).desc())
                        .limit(number))

            for review in response:
                books.append({
                    'book_id': review.book_id,
                    'rating': round(review.avg_rating, 1),
                })

            return books
        except Exception as e:
            print({'Error: ': e.args})
            raise None

    @staticmethod
    def get_average_by_month(month: int) -> Any:
        try:
            books = []
            response = (Review.select(Review.book_id, fn.AVG(Review.rating).alias('avg_rating'))
                        .where(fn.date_trunc('month', Review.create_date) == datetime.date(datetime.date.today().year, month, datetime.date.today().day))
                        .group_by(Review.book_id)
                        .order_by(fn.AVG(Review.rating).desc()))

            for review in response:
                books.append({
                    'book_id': review.book_id,
                    'rating': round(review.avg_rating, 1),
                })

            return books
        except Exception as e:
            print({'Error: ': e.args})
            raise None
