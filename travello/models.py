from django.db import models

# Create your models here.

class destination(models.Model):

    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to ='pics')
    offer = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name

   