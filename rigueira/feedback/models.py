from ckeditor.fields import RichTextField
from core.models import User
from django.core.exceptions import ValidationError
from django.db import models


class FeedBack(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    feedback = RichTextField()
    date_creat = models.DateField(auto_now_add=True)
    date_change = models.DateField(auto_now=True)
    authorized = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_change']
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'

    def save(self, *args, **kwargs):
        if self.user.user_type != 1:
            raise ValidationError(
                {
                    'user': (
                        'Somente é possível criar feedbacks, que o usuário seja um estudante'
                    )
                }
            )
        else:
            super().save(*args, **kwargs)




class Semestre(models.Model):
    class Materia(models.TextChoices):
        PORTUGUES = "Português"
        GEOGRAFIA = "Geografia"
        HISTORIA = "História"
        FISICA = "Física"
        MATEMATICA = "Matemática"
        CIENCIA = "Ciência"
        QUIMICA = "Química"

    class Semestre(models.TextChoices):
        PRIMEIRO = "1º semestre"
        SEGUNDO = "2º semestre"
        TERCEIRO = "3º semestre"
        QUARTO = "4º semestre"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ano = models.DateField(auto_now=True)
    semestre = models.IntegerField(choices=Semestre.choices)
    materia = models.CharField(max_length= 50,choices=Materia.choices)


class Nota(models.Model):
    nota = models.FloatField()
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
