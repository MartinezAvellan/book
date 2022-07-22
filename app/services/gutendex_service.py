import json
import requests


def get_books_api(url: str) -> dict:
    response = requests.request("GET", url, headers={}, data={})
    print('Response code {}, URL: {}'.format(response.status_code, url))
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return {
            'results': [],
            'next': None,
            'previous': None
        }
