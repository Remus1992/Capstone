# Generated by Django 2.0.1 on 2018-02-07 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180207_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]