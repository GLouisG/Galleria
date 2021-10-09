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
      self.picha.save_img()
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

    def test_get_by_loc(self):
        img = Image.get_by_loc('Nairobi, Kenya')
        self.assertTrue(len(img)>0)    

    def test_search(self):
        img = Image.img_searcher('Nature')
        self.assertTrue(len(img)>0)      
    def test_delete(self):
        self.picha.delete_img()
        self.assertTrue(len(Image.objects.all())==0)
    def test_update(self):
        updated=self.picha.img_updater('new.jpg', 'Hi')
        self.assertEqual(updated.photo, 'new.jpg')
        self.assertEqual(updated.description, 'Hi')

class CategoryTestClass(TestCase):

    def setUp(self):
        self.categ= Category(name='test')
        self.categ.save_category()
    def tearDown(self):
        Category.objects.all().delete()
    def test_save_category(self):
        self.assertTrue(len(Category.objects.all())==1) 
    def test_update_category(self):
        updated = Category.updater('test', 'new test')
        self.assertEqual(updated.name, 'new test')            
    def test_delete_category(self):
        deleted = self.categ.delete_category()
        self.assertTrue(len(Category.objects.all())==0)        

class LocationTestClass(TestCase):
    def setUp(self):
        self.Nairobi = Location(place='Nairobi')
        self.Nairobi.save_locale() 
    def tearDown(self):
        Location.objects.all().delete()
    def test_save_location(self):
        self.assertTrue(len(Location.objects.all())==1) 
    # def test_update_location(self):
    #     updated = self.Nairobi.updater('Nakuru')
    #     self.assertEqual(updated.place, 'Nakuru')            
    # def test_delete_location(self):
    #     deleted = self.Nairobi.delete_locale()
    #     self.assertTrue(len(Location.objects.all())==0)  