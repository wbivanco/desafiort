from apps.api.services import get_token


def test_get_token():
    res = get_token()
    assert res['status'] == 200
