
from .fixtures import get_response
from apps.api.services import get_publishings_more_expensive


def test_publishings_ordering():
    """
    Verifico que el listado de publicaciones este ordenado de mayor a menor por precio.
    """

    publishings = get_publishings_more_expensive()  # Obtengo toda la info de las publicaciones de la categoría
    data_results = publishings.get('results')  # De toda la data solo tomo las publicaciones

    higher = data_results[0].get('price')  # Tomo como valor más alto el pecio del primer registro
    orderly = True  # Bandera que me indica si la data esta ordenada

    # Recorro la data y verifico si esta ordenada de mayor a menor por precio
    for result in data_results:
        if higher < result.get('price'):
            orderly = False

    assert orderly == True


def test_reponse_code_200_publishings():
    """
    Pruebo si esta bien la ruta que paso como parametro.
    """

    res = get_response('https://api.mercadolibre.com/sites/MLA/search?category=MLA352679&sort=price_desc')

    assert res.status_code == 200
