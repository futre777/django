# Generated by Django 3.0.5 on 2020-05-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_post_ficheiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='referencia',
            field=models.URLField(default='none.com', max_length=500),
        ),
    ]
