import requests


def test_response_code_200_sellers():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
    }

    url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA352679&sort=price_desc"

    response = requests.get(url, headers)
    valor = response.json()
    print(valor)
    assert response.status_code == 200
