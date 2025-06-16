from django.db import models

# Create your models here.
class Message(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoyee = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.email})"