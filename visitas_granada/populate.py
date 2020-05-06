import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django

django.setup()

from visitas_granada.models import Visita, Comentario

if __name__ == "__main__":
    v = Visita(nombre="Alhambra", descripcion="La Alhambra es un complejo monumental sobre una ciudad palatina andalusí situado en Granada, España.", foto="alhambra.webp")
    v.save()
    c= Comentario(visita=v, texto="un lugar maravilloso")
    c.save()
    c = Comentario(visita=v, texto="Repetiré sin duda")
    c.save()

    v = Visita(nombre="Corral del Carbón",
               descripcion="El Corral del Carbón es un edificio del siglo XIV situado en la ciudad española de Granada, en la comunidad autónoma de Andalucía. Es la única alhóndiga nazarí conservada en su integridad en la península ibérica",
               foto="carbon.jpg")
    v.save()
    c = Comentario(visita=v, texto="un lugar maravilloso")
    c.save()
    c = Comentario(visita=v, texto="Repetiré sin duda")
    c.save()

    v = Visita(nombre="Monasterio de Cartuja",
               descripcion="El Real Monasterio de Nuestra Señora de la Asunción de la Cartuja, situado en la ciudad española de Granada, comunidad autónoma de Andalucía.",
               foto="cartuja.jpg")
    v.save()
    c = Comentario(visita=v, texto="un lugar maravilloso")
    c.save()
    c = Comentario(visita=v, texto="Repetiré sin duda")
    c.save()

    # ...

    print(Visita.objects.all())