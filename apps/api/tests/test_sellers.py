
from .fixtures import get_response


def test_error_idseller():
    """
    Verifica si el id del venderor pasado en el endpoint pertecene a un usuario de la plataforma.
    """

    seller_id = '22345342'

    res = get_response('https://api.mercadolibre.com/sites/MLA/search?seller_id=' + seller_id + '&category=MLA352679')

    json_data = res.json()
    assert len(json_data.keys()) == 10  # En caso de que el id pasado no pertenezca a un vendedor, el diccionario solo
    # devolverá 9 claves


def test_response_code_200_sellers():
    """
    Pruebo si esta bien la ruta que paso como parametro.
    """

    res = get_response('https://api.mercadolibre.com/sites/MLA/search?category=MLA352679&sort=price_desc')

    assert res.status_code == 200
