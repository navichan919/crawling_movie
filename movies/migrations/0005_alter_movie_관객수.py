# Generated by Django 4.2.7 on 2023-11-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0004_alter_movie_관객수"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="관객수",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
