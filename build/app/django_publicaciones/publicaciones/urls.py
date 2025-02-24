from django.urls import path
from .views import lista_publicaciones

urlpatterns = [
    path('', lista_publicaciones, name='lista_publicaciones'),
]
