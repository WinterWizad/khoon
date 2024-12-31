from django.db import models

# Create your models here.
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
<<<<<<< HEAD
from django.utils import timezone



=======
>>>>>>> 8c0dd8e8b724120e633de759ea8010c95d815f0e

class Doners(models.Model):
    name=models.CharField(max_length=50)
    phone= models.CharField(
        max_length=20,  # Adjust based on your needs
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],unique=True
    )
    address=models.CharField(max_length=50)
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
<<<<<<< HEAD
    lastDonatedDate=models.DateField(null=False,default=timezone.now)
=======
    lastDonatedDate=models.DateField(auto_now=True)
>>>>>>> 8c0dd8e8b724120e633de759ea8010c95d815f0e
    photo=models.ImageField(default="patient.webp", blank=True,null=False)
    slug=AutoSlugField(populate_from='phone',unique=True,null=True,default=None)
    username = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
     return self.name
    