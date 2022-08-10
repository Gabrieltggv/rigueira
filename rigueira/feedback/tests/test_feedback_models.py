import pytest
from feedback.models import FeedBack


@pytest.fixture()
def create_user_student(django_user_model):
    email = 'rogerio@teste.com'
    password = 'teste1'
    user = django_user_model.objects.create_user(
        email=email, password=password, user_type=1
    )
    return user


def test_create_feedback(create_user_student):
    user = create_user_student
    text = f"""
        Rigueira Acompanhamento Escolar 🔰
        Aluno (a): {user.first_name} {user.last_name}
        Turma: 8° Ano
        Colégio:
        ✅ Realizou:
            - Reforço na matéria de Redação com a produção e correção de um
            texto dissertativo/argumentativo sobre o tema: os estigmas em
            relação ao vírus HIV na sociedade brasileira.
        Observações:
            - A aluna apresentou um pouco de dificuldade quanto ao
            desenvolvimento do tema na construção do rascunho da redação, mas
            obteve um avanço após a explicação e correção do rascunho,
            melhorando significante na reconstrução do texto.
            Faltou refazer apenas a conclusão.
            Boa noite! 🌙"""
    FeedBack.objects.create(user=user, feedback=text)
    assert FeedBack.objects.count() == 1
