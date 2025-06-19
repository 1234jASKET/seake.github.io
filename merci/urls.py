from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # ceci appelle la vue "accueil"
    path('contact/', views.contact, name='contact'),
    path('messages/', views.messages_liste, name='messages_liste'),
    path('journal/', views.journal, name='journal'),
    path('parole/', views.parole, name='parole')
]