# Generated by Django 3.0.5 on 2020-05-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200504_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='nome',
            field=models.CharField(max_length=120),
        ),
    ]
