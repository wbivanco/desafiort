import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


def get_sellers_by_category(params={}):
    response = generate_request('https://api.mercadolibre.com/categories/MLA352679', params)

    if response:
       return response
    return ''


def get_publishings_more_expensive(params={}):
    response = generate_request('https://api.mercadolibre.com/sites/MLA/search?category=MLA352679', params)

    if response:
       return response
    return ''