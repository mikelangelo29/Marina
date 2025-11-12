from django.urls import path
from . import views


urlpatterns = [
path('nat/', views.natural, name='natura'),

]