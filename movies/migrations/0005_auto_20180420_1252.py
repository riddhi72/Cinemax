# Generated by Django 2.0.3 on 2018-04-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20180419_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movieName',
            field=models.CharField(max_length=30),
        ),
    ]