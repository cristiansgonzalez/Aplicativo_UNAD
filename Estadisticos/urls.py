from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("contacto/", views.contacto),
    path("comentarios/", views.comentarios),
    path("descargar/", views.descargar)
]