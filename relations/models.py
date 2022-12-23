from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    bio = models.TextField(blank=True)
    image =models.ImageField(upload_to='profile', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Adress(models.Model):
    name = models.CharField(max_length=20)
    addredd = models.CharField(max_length=150)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.user.username}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name