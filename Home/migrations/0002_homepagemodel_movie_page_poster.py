# Generated by Django 3.2 on 2021-11-24 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagemodel',
            name='movie_page_poster',
            field=models.ImageField(blank=True, null=True, upload_to='Posters/MoviePage/'),
        ),
    ]