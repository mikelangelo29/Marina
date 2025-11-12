from django.shortcuts import render

# Create your views here.
from .models import Natura

def natural (request):
    specie=Natura.objects.all()
    return render(request, "natura.html",{'specie':specie})