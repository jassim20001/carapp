from django.db import models

# Create your models here.
class Carsone(models.Model):
    name=models.CharField(max_length=300)
    model=models.DateField()
    type=models.CharField(max_length=400)
    price=models.IntegerField()
    slug=models.SlugField(null=True,blank=True)
    description=models.TextField(max_length=4000)
    img=models.ImageField(upload_to='photo')
    speed=models.IntegerField(default=0)
    color=models.CharField(max_length=100)
    horspwoer=models.IntegerField(default=0)
class Carstwo(models.Model):
    name=models.CharField(max_length=300)
    model=models.DateField()
    type=models.CharField(max_length=400)
    price=models.IntegerField()
    slug=models.SlugField()
    description=models.TextField(max_length=4000)
    img=models.ImageField(upload_to='photo')
    speed=models.IntegerField(default=0)
    color=models.CharField(max_length=100)
    horspwoer=models.IntegerField(default=0)

class Serves(models.Model):
    img=models.ImageField(upload_to='photo')
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=5000)
class Conect(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    message=models.TextField(max_length=5000)