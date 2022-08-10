from ckeditor.fields import RichTextField
from core.models import User
from django.core.exceptions import ValidationError
from django.db import models


class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = RichTextField()
    date_creat = models.DateField(auto_now_add=True)
    date_change = models.DateField(auto_now=True)
    authorized = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

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
