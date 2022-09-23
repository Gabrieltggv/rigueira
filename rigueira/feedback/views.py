from django.shortcuts import HttpResponse, render

from .models import Nota


def dashboard(request) -> HttpResponse:
    notas = {Nota.objects.filter(semestre=i) for i in range(5, 1)}
    ctx = {'semestres': notas}
    return render(request, 'feedback/dashboard.html', ctx)
