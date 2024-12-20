# Generated by Django 5.1.3 on 2024-12-06 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movie_app.director'),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie'),
        ),
    ]
