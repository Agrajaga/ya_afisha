# Generated by Django 4.0.5 on 2022-06-13 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description_short', models.CharField(max_length=500)),
                ('description_long', models.TextField()),
                ('coord_lng', models.FloatField()),
                ('coord_lat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
            ],
        ),
    ]
