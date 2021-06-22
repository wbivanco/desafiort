import requests


def test_no_id_seller_send():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA352679&sort=price_desc"

    response = requests.get(url, headers)
    valor = response.json()
    print(valor)
    assert response.status_code == 200


def test_reponse_code_200_publishings():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA352679&sort=price_desc"

    response = requests.get(url, headers)
    valor = response.json()
    print(valor)
    assert response.status_code == 200
