# Generated by Django 3.2.7 on 2021-11-23 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0008_docente_nodocente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodocente',
            name='oficina',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
        migrations.DeleteModel(
            name='NoDocente',
        ),
    ]
