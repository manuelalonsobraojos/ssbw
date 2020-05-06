from django.db import models
from django import forms
from .validators import validateCapital

class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    foto = models.FileField(upload_to='fotos', blank=True)

class Comentario(models.Model):
    visita = models.ForeignKey(Visita, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['nombre', 'descripcion', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'size': 40}),
            'descripción': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'foto': forms.FileInput()
		}



