# Generated by Django 4.2.13 on 2024-05-28 23:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=100000)),
                ('time', models.TimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
