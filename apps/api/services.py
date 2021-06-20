import requests


def generate_request(url):
    """
    Obtiene la respuesta de la url de los parametros que se recibe la función,  verifica si la misma es correcta y si es
    así devuelve la misma en un json.
    """

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


def get_sellers_by_category():
    """
    Obtiene el listado de los vendores.
    """

    response = generate_request('https://api.mercadolibre.com/sites/MLA/search?category=MLA352679')

    if response:
        return response
    return ''


def get_publishings_more_expensive():
    """
    Obtiene el listado de las publicaciones.
    """

    response = generate_request('https://api.mercadolibre.com/sites/MLA/search?category=MLA352679&sort=price_desc')

    if response:
        return response
    return ''
