# Generated by Django 4.1.3 on 2022-12-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('relacion', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=10)),
            ],
        ),
    ]
