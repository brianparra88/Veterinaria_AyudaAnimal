# Generated by Django 3.1.3 on 2023-11-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='especie',
            field=models.CharField(choices=[('1', 'Gato'), ('2', 'Perro'), ('3', 'Exótico')], max_length=200),
        ),
    ]
