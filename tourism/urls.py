from django.urls import path
from . import views

urlpatterns = [
path('bandb/', views.hotel, name='b&b'),
path('pubs/', views.risto, name='pubs'),
path('lidi/', views.lidi, name='lidi')

]