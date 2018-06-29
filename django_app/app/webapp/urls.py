from django.urls import path

from . import views

app_name = 'webapp'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('registrarse/', views.registrarse, name = 'registrarse'),
    path('reservas/', views.reservas, name = 'reservas'),
]
