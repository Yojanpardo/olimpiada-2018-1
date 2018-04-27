# Generated by Django 2.0.4 on 2018-04-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=255, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('carrera', models.CharField(max_length=255)),
            ],
        ),
    ]
