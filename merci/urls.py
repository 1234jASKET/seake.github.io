from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # ceci appelle la vue "accueil"
    path('contact/', views.contact, name='contact'),
    path('messages/', views.messages_liste, name='messages_liste'),
]