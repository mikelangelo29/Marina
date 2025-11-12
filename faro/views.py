from django.shortcuts import render
from news.models import News 
from tourism.models import Hotel


# Create your views here.

def home (request):
    newscroll=News.objects.all()
    context = {"newscroll": newscroll}
    return render (request, 'farohp.html', context)

def turismo (request):
    return render (request, 'turismo.html')

def storia (request):
    return render (request, "storiahp.html")

def storia1 (request):
    return render (request, "storia_bonifica.html")

def storia2 (request):
    return render (request, "storia_insed.html")


def biblio (request):
    return render (request, "storia_biblio.html")

def chisiamo (request):
    return render (request, "chisiamo.html")

def sitemap (request):
   return render (request, "sitemap.xml")

def search (request):
    if 'q' in request.GET and request.GET ['q']:
        q= request.GET ['q']
        news= News.objects.filter(descrizione__icontains = q)
        news=News.objects.filter(titolo__icontains = q)
        hotels= Hotel.objects.filter(titolo__icontains = q)
        context = {'news': news, 'hotels':hotels}
        return render(request, 'search.html', context)
    else:
        return render (request, "search.html")
    
