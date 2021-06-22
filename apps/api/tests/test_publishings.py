
from .fixtures import get_response


def test_error_idseller():
    """
    Verifica si el id del venderor pasado en el endpoint pertecene a un usuario de la plataforma.
    """

    res = get_response('https://api.mercadolibre.com/sites/MLA/search?seller_id=22345342&category=MLA352679')

    json_data = res.json()
    assert len(json_data.keys()) == 10


def test_reponse_code_200_publishings():
    """
    Pruebo si esta bien la ruta que paso como parametro.
    """

    res = get_response('https://api.mercadolibre.com/sites/MLA/search?category=MLA352679&sort=price_desc')

    assert res.status_code == 200
