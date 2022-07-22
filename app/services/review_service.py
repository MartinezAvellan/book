from playhouse.shortcuts import model_to_dict
from app.models.review import Review


class ReviewService:

    @staticmethod
    def create_review(review: dict) -> dict:
        try:
            response = Review.create(
                book_id=review.get('book_id'),
                rating=review.get('rating'),
                review=review.get('review'),
            )
            if response is not None:
                result = model_to_dict(response)
                print({'message': 'review created', 'book_id': int(review.get('book_id')), 'review': result})
                review: dict = {
                    'id': result.get('id'),
                    'book_id': result.get('book_id'),
                    'rating': result.get('rating'),
                    'review': result.get('review'),
                }

                return review
            else:
                raise Exception(response)
        except Exception as e:
            print({'Error: ': 'review cant be created', 'book_id': int(review.get('user_id')), 'exception': e.args})
            return None

    @staticmethod
    def get_reviews_and_average(book_id: int) -> dict:
        try:
            response = Review.select().where(Review.book_id == book_id).order_by(Review.id)
            result: list = list(response.dicts())
            if result is not None:
                reviews = []
                sum_ratings: int = 0
                total_ratings: int = len(result)
                rating: float = 0.0
                for r in result:
                    reviews.append(r.get('review'))
                    sum_ratings = sum_ratings + int(r.get('rating'))

                rating: float = sum_ratings / total_ratings
                return {
                    'book_id': book_id,
                    'rating': rating,
                    'reviews': reviews
                }
            else:
                return None
        except Exception as e:
            print({'Error: ': e.args})
            raise None
