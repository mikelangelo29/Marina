from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator
from django.views.generic import DetailView


# Create your views here.

def news (request):
    notizie=News.objects.all()
    paginator= Paginator(notizie,8)
    page= request.GET.get("pagina")
    page_obj = paginator.get_page(page)

    return render(request, "news.html",{ "notizie":page_obj})

class SingoliArticoli (DetailView):
    model= News
    template_name= "singolo.html"
