from app.services.gutendex_service import get_books_by_title
from app.utils.constants import GUTENDEX_URL
from app.utils.utils import find_number_of_page


def search_book_by_title(title: str, args: dict) -> dict:
    books: dict = []
    title_url = title
    if args.get('page') is not None:
        title_url = str(title + '&page=' + str(args.get('page')))

    data = get_books_by_title(GUTENDEX_URL.format(title_url.replace(' ', '%20')))
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
