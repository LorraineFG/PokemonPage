# Generated by Django 2.2.26 on 2022-02-06 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='urlpokemon',
            field=models.URLField(blank=True, null=True, verbose_name='Detalhe Pokemon'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='urlimagem',
            field=models.URLField(blank=True, null=True),
        ),
    ]
