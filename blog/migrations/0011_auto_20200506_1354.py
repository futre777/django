# Generated by Django 3.0.5 on 2020-05-06 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200505_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sobre_mim',
            new_name='frase_do_dia',
        ),
    ]
