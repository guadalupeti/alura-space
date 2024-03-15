# Generated by Django 5.0.3 on 2024-03-15 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(choices=[(True, 'Publicado'), (False, 'Não Publicado')], default=False),
        ),
    ]
