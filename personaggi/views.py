from django.shortcuts import render
from .models import Personaggi

# Create your views here.


def perso (request):
    per=Personaggi.objects.all()
    return render(request, "storia_personaggi.html",{'per':per})
