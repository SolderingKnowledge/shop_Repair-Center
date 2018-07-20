from django.db import models

# Create your models here.



class Merchandise(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=40.00)
    image           = models.ImageField(upload_to="merchandise/", null=True, blank=True)


    def __str__(self):
    	return self.title
