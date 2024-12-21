# Generated by Django 5.1.4 on 2024-12-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='original_title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]