from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password= models.CharField(max_length=100) #makemigrations krne se model class se hmara sql queries ko generate ho jata h or usko execute krne ke liye migrate krna pdta h
