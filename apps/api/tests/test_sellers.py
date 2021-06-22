
from .fixtures import get_response


def test_response_code_200_sellers():
    """
    Pruebo si esta bien la ruta que paso como parametro.
    """

    res = get_response('https://api.mercadolibre.com/sites/MLA/search?category=MLA352679&sort=price_desc')

    assert res.status_code == 200
