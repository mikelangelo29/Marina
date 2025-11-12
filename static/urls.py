from django.contrib import admin
from django.urls import path, include
from faro import views 
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage' ),
    path('turismo/', views.turismo, name='turismo'),
    path('tourism/', include('tourism.urls')), 
    path('news/', include ('news.urls')),
    path('search/', views.search, name='cerca'),
    path('storia/', views.storia, name='storia'),
    path('bonifica/', views.storia1, name='stornara'),
    path('insediamenti/', views.storia2, name='insediamenti'),
    path('personaggi/', include ('personaggi.urls')),
    path('biblio/', views.biblio, name='biblio'),
    path('natura/', include('natura.urls')),
    path('50_60/', include('cinquanta.urls')),
    path('chi_siamo/', views.chisiamo, name='chisiamo'),
    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
