# Create your tests here.


def test_url_login(client):
    resp = client.get('/')
    assert resp.status_code == 200
