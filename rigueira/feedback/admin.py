from django.contrib import admin
from feedback.models import FeedBack, Nota, Semestre

# Register your models here.
admin.site.register(FeedBack)
admin.site.register(Semestre)
admin.site.register(Nota)
