from app.services.book_service import search_book_by_title, search_book_by_id


class TestBookService:

    def test_search_book_by_title(self):
        title: str = 'aa'
        args: dict = {'page': 3}
        result = search_book_by_title(title, args)
        assert result.get('next') == 4
        assert result.get('previous') == 2
        assert result.get('books') is not []

    def test_search_book_by_id(self):
        book_id: str = '84'
        result = search_book_by_id(book_id)
        assert result.get('id') == int(book_id)
        assert result.get('title') == 'Frankenstein; Or, The Modern Prometheus'

    def test_search_book_by_id_none(self):
        book_id: str = '0'
        result = search_book_by_id(book_id)
        assert result is None
