# Generated by Django 2.2.7 on 2019-11-30 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luna', '0002_auto_20191123_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='nombre_usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='agendaservicio',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luna.nombre_usuario'),
        ),
    ]