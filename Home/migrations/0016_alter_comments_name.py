# Generated by Django 3.2 on 2021-11-29 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_alter_comments_movie_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(default='Guest', max_length=200),
        ),
    ]
