from django.shortcuts import render
from .models import Image, Location, Category
# Create your views here.
def landing(request):
    pics = Image.get_all()
    areas = Location.get_all()
    categs = Category.get_all()
    return render(request, 'index.html', {"pics": pics, "areas":areas, "categs":categs})
    
