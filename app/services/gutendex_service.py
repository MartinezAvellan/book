import json
import requests


def get_books_by_title(url: str) -> dict:
    response = requests.request("GET", url, headers={}, data={})
    print('Response code {}. body: {}. URL: {}'.format(response.status_code, response.text, url))
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return {
            'results': [],
            'next': None,
            'previous': None
        }
