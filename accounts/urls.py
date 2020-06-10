from django.urls import path

from . import views

urlpatterns = [
    path('Slogin', views.Slogin, name='Slogin'),
    path('Flogin', views.Flogin, name='Flogin'),
]