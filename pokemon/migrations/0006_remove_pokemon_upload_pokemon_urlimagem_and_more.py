# Generated by Django 4.0.1 on 2022-01-25 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0005_auto_20220125_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='upload',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='urlimagem',
            field=models.CharField(max_length=300, null=True, verbose_name='urlimage'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]