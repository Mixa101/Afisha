# Generated by Django 5.1.3 on 2024-12-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_movie_director_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(),
        ),
    ]
