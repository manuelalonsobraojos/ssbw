# Generated by Django 3.0.5 on 2020-05-06 16:48

from django.db import migrations, models
import visitas_granada.validators


class Migration(migrations.Migration):

    dependencies = [
        ('visitas_granada', '0002_visita_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='descripcion',
            field=models.CharField(max_length=1000, validators=[visitas_granada.validators.validateCapital]),
        ),
    ]
