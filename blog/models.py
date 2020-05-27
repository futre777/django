from django.db import models
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    frase_do_dia = models.TextField()
    imagem = models.ImageField(default='static/img/author_image.png', upload_to='profile_pics')
    imagem_bio = models.ImageField(upload_to='profile_pics/bio_pics')

    def __str__(self):
        return f'Perfil de {self.nome}'

    def save(self):
        super().save()

        img = Image.open(self.imagem.path)
        img_bio = Image.open(self.imagem_bio.path)

        if img.height > 200 or img.width > 200:
            area = (50, 0, 896, 854)
            cropped_img = img.crop(area)
            cropped_img = cropped_img.resize((190, 190), Image.ANTIALIAS)   
            cropped_img.save(self.imagem.path)

        if img_bio.height > 900 or img_bio.width > 900:
            area = (50, 0, 896, 854)
            cropped_img = img_bio.crop(area)
            cropped_img = cropped_img.resize((896, 854), Image.ANTIALIAS) 
            cropped_img.save(self.imagem_bio.path)    

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    abstracto = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    imagem = models.ImageField(upload_to='post_pics')
    referencia = models.URLField(default='none.com', max_length=500)
    ficheiro = models.FileField(default='none', upload_to='documents')


    def __str__(self):
        return self.titulo  

    def save(self):
        super().save()

        img = Image.open(self.imagem.path)
        

        if img.height > 800 or img.width > 500:
            img = img.resize((750, 500), Image.ANTIALIAS)   
            img.save(self.imagem.path)    

class Gallery(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='gallery_pics') 
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    def save(self):
        super().save()

        img = Image.open(self.imagem.path)
        
        if img.height > 750 or img.width > 500:
            img = img.resize((750, 500), Image.ANTIALIAS)   
            img.save(self.imagem.path)    

class Message(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome

class Contact(models.Model):
    email = models.EmailField()
    numero = models.CharField(max_length=100)

    def __str__(self):
        return self.email
        
