# Generated by Django 2.2.7 on 2019-11-30 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luna', '0003_auto_20191130_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaservicio',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
        migrations.DeleteModel(
            name='nombre_usuario',
        ),
    ]
