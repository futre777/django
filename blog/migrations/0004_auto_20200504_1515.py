# Generated by Django 3.0.5 on 2020-05-04 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='imagem_bio',
            field=models.ImageField(upload_to='profile_pics/bio_pics'),
        ),
    ]
