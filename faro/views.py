from django.shortcuts import render
from news.models import News 
from tourism.models import Hotel
from django.db.models import Q

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

def search(request):
    q = request.GET.get("q", "").strip()
    news = []

    if q:
        news = News.objects.filter(
            Q(titolo__icontains=q) | Q(descrizione__icontains=q)
        )

    context = {"news": news, "q": q}
    return render(request, "search.html", context)
    
