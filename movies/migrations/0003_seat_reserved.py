# Generated by Django 2.0.3 on 2018-04-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]