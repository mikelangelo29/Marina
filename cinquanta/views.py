from django.shortcuts import render


from .models import Anni50

def cinquanta (request):
    recente=Anni50.objects.all()
    return render(request, "storia_cinquanta.html",{'recente':recente})