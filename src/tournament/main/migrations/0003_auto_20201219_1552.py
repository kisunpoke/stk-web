# Generated by Django 3.1.4 on 2020-12-19 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201219_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappool',
            name='display_color',
            field=models.CharField(default='#FF000033', help_text='RGBA hex (as #RRGGBBAA), webpage-compatible.', max_length=9),
        ),
    ]
