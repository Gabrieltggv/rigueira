import pytest


@pytest.fixture()
def create_user_student(django_user_model):
    email = 'rogerio@teste.com'
    password = 'teste1'
    user = django_user_model.objects.create_user(
        email=email, password=password, user_type=1
    )
    return user


def test_tipo_student_usuario(create_user_student):
    user = create_user_student
    assert user.user_type == 1
