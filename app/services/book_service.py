from app.services.gutendex_service import get_books_api
from app.utils.constants import GUTENDEX_URL
from app.utils.utils import find_number_of_page


def search_book_by_title(title: str, args: dict) -> dict:
    books: dict = []
    title_url: str = title
    if args.get('page') is not None:
        title_url = str(title + '&page=' + str(args.get('page')))

    data: dict = get_books_api(GUTENDEX_URL + '?search=' + title_url.replace(' ', '%20'))
    for result in data['results']:
        if title in result['title']:
            books.append({
                'id': result['id'],
                'title': result['title'],
                'authors': result['authors'],
                'languages': result['languages'],
                'download_count': result['download_count']
            })

    return {
        'next': find_number_of_page(data['next']),
        'previous': find_number_of_page(data['previous']),
        'books': books
    }


def search_book_by_id(book_id: str) -> dict:
    data: dict = get_books_api(GUTENDEX_URL + '?ids=' + book_id)
    for result in data['results']:
        return {
            'id': result['id'],
            'title': result['title'],
            'authors': result['authors'],
            'languages': result['languages'],
            'download_count': result['download_count']
        }

    return None
