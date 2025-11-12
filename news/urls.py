
from django.urls import path
from . import views
from .views import SingoliArticoli

urlpatterns = [
path('notizie/', views.news, name='notizie'),
path('articolo/<int:pk>', SingoliArticoli.as_view(), name='singolo')

]
