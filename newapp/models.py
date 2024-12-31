from django.db import models
# from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils.text import slugify

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
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)



    slug=models.SlugField(unique=True,null=True,default=None,blank=True)

    def save(self, *args, **kwargs):   
        if not self.slug:     
            self.slug = generate_unique_slug(self, self.name)
            super().save(*args, **kwargs)

    def __str__(self):
     return self.name
    

# uniques slug generator
def generate_unique_slug(instance, name, slug_field='slug'):
    """
    Generates a unique slug for a model instance based on a given title.
    If a slug already exists, appends a number to the slug to make it unique.

    Args:
        instance (models.Model): The model instance.
        title (str): The title or string to base the slug on.
        slug_field (str): The slug field name in the model.

    Returns:
        str: A unique slug.
    """
    newname=name.lower()
    print("New slug is:")
    print(newname)
    slug = slugify(newname)
    unique_slug = slug
    model_class = instance.__class__
    
    # Check if slug already exists and append number if necessary
    num = 1
    while model_class.objects.filter(**{slug_field: unique_slug}).exists():
        unique_slug = f'{slug}-{num}'
        num += 1
        
    return unique_slug

