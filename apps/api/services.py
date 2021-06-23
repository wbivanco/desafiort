
from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint

import requests

# Defining the host, defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host="https://api.mercadolibre.com"
)


def generate_request(url):
    """
    Obtiene la respuesta de la url de los parametros que se recibe la función,  verifica si la misma es correcta y si es
    así devuelve la misma en un json.
    """

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


def get_sellers_by_category(offset,limit=50):
    """
    Obtiene el listado de las publicaciones por rango de 50 en la categoria MLA352679.
    """

    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA352679' + '&offset=' + str(offset) + '&limit=' + str(limit)
    response = generate_request(url)

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


def get_info_seller(id):
    """
    Obtiene la información de un vendedor en la categoría MLA352679.
    """
    url = 'https://api.mercadolibre.com/sites/MLA/search?seller_id=' + str(id) + '&category=MLA352679'
    response = generate_request(url)

    if response:
        return response
    return ''


def get_token():
    # Enter a context with an instance of the API client
    with meli.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = meli.OAuth20Api(api_client)
        grant_type = 'refresh_token'  # str
        client_id = '6092241007629087'  # Your client_id
        client_secret = '7Y0a0yhLw8c8XZ1OxWVpIbYc6BNX079a'  # Your client_secret
        redirect_uri = 'https://www.mercadolibre.com.ar/'  # Your redirect_uri
        code = 'TG-60d33aa81ea744000881f7ec-85614757'  # The parameter CODE
        refresh_token = 'TG-60d33c79c6805b00071cdd0b-85614757'  # Your refresh_token

    try:
        # Request Access Token
        api_response = api_instance.get_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret,
                                              redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
        # pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling OAuth20Api->get_token: %s\n" % e)