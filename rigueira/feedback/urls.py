from django.urls import path

from .views import dashboard

app_name = 'feedback'
urlpatterns = [path('dashboard', dashboard, name='dashboard')]
