# Generated by Django 4.0.5 on 2022-06-13 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeimage',
            name='link',
        ),
        migrations.AddField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='placeimage',
            name='index',
            field=models.PositiveSmallIntegerField(null=True, unique=True),
        ),
    ]
