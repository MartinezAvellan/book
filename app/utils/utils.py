
def find_number_of_page(url: str) -> int:
    page: int = None
    if url is not None and 'page=' in url:
        start = url.find("?page=") + len("?page=")
        end = url.find("&")
        page = int(url[start:end])

    return page

