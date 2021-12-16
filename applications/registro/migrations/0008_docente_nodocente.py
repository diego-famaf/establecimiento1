# Generated by Django 3.2.7 on 2021-11-23 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0007_auto_20211014_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoDocente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('full_name', models.CharField(blank=True, max_length=150, verbose_name='Nombre Completo')),
                ('age', models.IntegerField(verbose_name='Edad')),
                ('job', models.CharField(choices=[('1', 'No Docente')], max_length=50, verbose_name='Cargo')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='foto')),
                ('oficina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.oficina')),
            ],
            options={
                'verbose_name': 'NoDocente',
                'verbose_name_plural': 'NoDocentes',
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('full_name', models.CharField(blank=True, max_length=150, verbose_name='Nombre Completo')),
                ('age', models.IntegerField(verbose_name='Edad')),
                ('job', models.CharField(choices=[('0', 'Docente')], max_length=50, verbose_name='Cargo')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='foto')),
                ('materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.materia')),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
            },
        ),
    ]
