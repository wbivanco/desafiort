from apps.api.services import get_token


def test_get_token():
    res = get_token()
    print(res['status'])
    assert res['status'] == 400
