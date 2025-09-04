from django.contrib import admin
from django.urls import path
from miPrimerApp.views import pagina_inicio, galeria_fotografias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_inicio, name='inicio'),
    path('fotos/', galeria_fotografias, name='fotos'),
]