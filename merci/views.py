from django.shortcuts import render
from .forms import ContactForm
from .models import Message, Article  # ✅ Regroupement efficace

# -------------------
# PAGE D'ACCUEIL
# -------------------
def accueil(request):
    return render(request, 'merci/accueil.html')


# -------------------
# PAGE DE CONTACT
# -------------------
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                nom=form.cleaned_data['nom'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'merci/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'merci/contact.html', {'form': form})


# -------------------
# LISTE DES MESSAGES
# -------------------
def messages_liste(request):
    messages = Message.objects.all().order_by('-date_envoyee')
    return render(request, 'merci/messages_liste.html', {'messages': messages})


# -------------------
# PAGE DU JOURNAL
# -------------------
def journal(request):
    articles = Article.objects.order_by('-date_pub')
    return render(request, 'merci/journal.html', {'articles': articles})


# -------------------
# PAGE PAROLE DU JOUR
# -------------------
def parole(request):
    return render(request, 'merci/parole.html')