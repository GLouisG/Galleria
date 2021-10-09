from django.db import models


# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length =60)



class Location(models.Model):
  place = models.CharField(max_length =60)  
  


class Image(models.Model):
  photo = models.ImageField(upload_to='photos/', default='SOMETHING')
  location = models.ForeignKey('Location', on_delete=models.CASCADE, )
  category = models.ForeignKey('Category', on_delete=models.CASCADE,)
