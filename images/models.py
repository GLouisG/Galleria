from django.db import models


# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length =60)

  def __str__(self):
      return self.name
  def save_category(self):
    self.save()

class Location(models.Model):
  place = models.CharField(max_length =50)  

  def save_locale(self):
    self.save()
  def __str__(self):
      return self.place

class Image(models.Model):
  title = models.CharField(max_length=20)
  description = models.TextField()
  photo = models.ImageField(upload_to='photos/', default='SOMETHING')
  location = models.ForeignKey('Location', on_delete=models.CASCADE, )
  category = models.ForeignKey('Category', on_delete=models.CASCADE,)


  def save_img(self):
    self.save()
  def delete_img(self):
    self.delete()
  # def img_updater(self, new_pic, desc,):
  #   try:
  #     self.photo = new_pic
  #     self.description = desc
  #     self.save()
  #     return self
  #   except self.DoesNotExist:
  #     print('Image not found')    
  # @classmethod
  # def get_all(cls,):
  #  photos = cls.objects.all()
  #  return photos
  def __str__(self):
      return self.title
