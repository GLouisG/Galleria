from django.db import models


# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length =60)

  def __str__(self):
      return self.name

  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()

  @classmethod
  def updater(cls, old_name, jina):
    try:
      categ  = Category.objects.get(name= old_name)
      categ.name = jina
      categ.save()
      return categ
    except Category.DoesNotExist:
      print('That does not exist') 

  @classmethod
  def get_all(cls,):
   categories = cls.objects.all()
   return categories
class Location(models.Model):
  place = models.CharField(max_length =50)  

  def save_locale(self):
    self.save()

  def delete_locale(self):
    self.delete()    

  def updater(self, loc):
    try:
      self.place = loc
      self.save()
      return self
    except self.DoesNotExist:
      print('The location you gave does not exist in our records')     

  @classmethod
  def get_all(cls,):
   locations = cls.objects.all()
   return locations

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

  def img_updater(self, new_pic, desc,):
    try:
      self.photo = new_pic
      self.description = desc
      self.save()
      return self
    except self.DoesNotExist:
      print('Image not found')  

  @classmethod
  def get_all(cls,):
   photos = cls.objects.all()
   return photos

  @classmethod 
  def get_by_id(cls, id):
    photo = cls.objects.filter(id=id)
    return photo

  @classmethod
  def get_by_loc(cls, loc):
    photos = cls.objects.filter(location__place__contains = loc)
    return photos 


  @classmethod
  def img_searcher(cls, categ):
    photos = cls.objects.filter(category__name__contains = categ)
    return photos    

  def __str__(self):
      return self.title
