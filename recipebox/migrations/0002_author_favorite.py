# Generated by Django 3.0.6 on 2020-06-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorite',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorited', to='recipebox.RecipeModel'),
        ),
    ]
