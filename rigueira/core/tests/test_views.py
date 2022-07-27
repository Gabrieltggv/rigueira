import pytest


@pytest.fixture()
def create_user(django_user_model):
    email = 'teste@te.com'
    password = 'teste123'
    user = django_user_model.objects.create_user(
        email=email, password=password
    )
    return user


def test_status_200(client):
    resp = client.get('/')
    assert resp.status_code == 200


@pytest.mark.django_db()
def test_redirect_user_logado(client, create_user):
    dict_post = {'email': 'teste@te.com', 'password': 'teste123'}
    resp = client.post('/', dict_post)
    assert resp.status_code == 302


@pytest.mark.django_db()
def test_user_nao_cadastrado(client):
    dict_post = {'email': 'teste_invalido@te.com', 'password': 'teste123'}
    resp = client.post('/', dict_post)
    assert resp.status_code == 200
