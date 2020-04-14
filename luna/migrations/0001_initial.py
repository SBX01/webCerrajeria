# Generated by Django 2.2.7 on 2019-11-21 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('passw', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='agendaServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=25)),
                ('tipoServicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luna.Servicio')),
            ],
        ),
    ]
