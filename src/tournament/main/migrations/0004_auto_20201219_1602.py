# Generated by Django 3.1.4 on 2020-12-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201219_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='duration',
            field=models.IntegerField(help_text="Map's duration in seconds, from first to last note (including breaks)", verbose_name='Total length'),
        ),
    ]