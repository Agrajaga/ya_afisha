# Generated by Django 3.2.13 on 2022-06-16 20:08

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_placeimage_options_alter_placeimage_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coord_lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coord_lng',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(max_length=500, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
