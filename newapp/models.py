from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Emergencies(models.Model):
    name=models.CharField(max_length=20,unique=True)
    hospital=models.CharField(max_length=30)
    age=models.IntegerField()
    choice=(('B+','B+'),
            ('A+','A+'),
            ('A','A'),
            ('B','B'),
            ('O','O'),
            ('O+','O+'),
            ('AB','AB'),
            ('AB+','AB+')
           )
    blood=models.CharField(max_length=10,choices=choice)
    reason=models.CharField(max_length=200)
    date=models.DateField(auto_now=True)
    photo=models.ImageField(default='patient.webp', blank=True)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)


    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
     return self.name
    

# Create your models here.
