from django.shortcuts import render
from .forms import ContactForm
from .models import Message  # on importe ton modèle

def accueil(request):
    return render(request, 'merci/accueil.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Sauvegarder les données dans la base
            Message.objects.create(
                nom=form.cleaned_data['nom'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'merci/contact_success.html')  # page de succès
    else:
        form = ContactForm()
    return render(request, 'merci/contact.html', {'form': form})

from .models import Message  # déjà importé si tu as suivi l'étape précédente

def messages_liste(request):
    messages = Message.objects.all().order_by('-date_envoyee')  # les plus récents d'abord
    return render(request, 'merci/messages_liste.html', {'messages': messages})