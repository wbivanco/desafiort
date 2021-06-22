import requests


def get_response(url):
    """
    Funciòn que me permite conectar a una ruta, y devuelve un resultado.
    """

    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    response = requests.get(url, headers)

    return response