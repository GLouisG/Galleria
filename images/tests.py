from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class ImageTestClass(TestCase):


    def setUp(self):

      self.Nature= Category(name='nature')
      self.Nature.save_category()  
     
      self.Nairobi= Location(place='Nairobi, Kenya')
      self.Nairobi.save_locale() 

      self.picha= Image(title= 'Test', photo ='test.jpg' ,description='Random Words', category=self.Nature, location = self.Nairobi)
      self.picha.save()
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()    
    def test_get_all(self):
        imgs = Image.get_all()
        self.assertTrue(len(imgs)>0)

    def test_get_by_id(self):
        img = Image.get_by_id(1)
        self.assertTrue(len(img)>0)

    # def test_get_by_loc(self):
    #     img = Image.get_by_loc('Nairobi, Kenya')
    #     self.assertTrue(len(img)>0)    

    # def test_search(self):
    #     img = Image.img_searcher('Nature')
    #     self.assertTrue(len(img)>0)      
    # def test_delete(self):
    #     self.picha.delete_img()
    #     self.assertTrue(len(Image.objects.all())==0)
    # def test_update(self):
    #     updated=self.picha.img_updater('new.jpg', 'Hi')
    #     self.assertEqual(updated.photo, 'new.jpg')
    #     self.assertEqual(updated.description, 'Hi')

# class CategoryTestClass(TestCase):
#   abc = 'abc'

# class LocationTestClass(TestCase):
#   abc = 'abc'