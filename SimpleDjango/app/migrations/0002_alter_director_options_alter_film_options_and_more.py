# Generated by Django 4.1.2 on 2022-10-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='director',
            options={'ordering': ['name'], 'verbose_name': 'Director', 'verbose_name_plural': 'Directors'},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['year', 'title'], 'verbose_name': 'Film', 'verbose_name_plural': 'Films'},
        ),
        migrations.AddField(
            model_name='film',
            name='directiors',
            field=models.ManyToManyField(to='app.director'),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.TextField(max_length=128),
        ),
        migrations.DeleteModel(
            name='FilmDirector',
        ),
    ]
