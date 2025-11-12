from django.urls import path
from . import views


urlpatterns = [
    path('pstorici/', views.perso, name='personaggi' )
]

