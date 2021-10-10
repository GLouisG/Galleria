from django.shortcuts import render
from .models import Image, Location, Category
from django.http import HttpResponse, Http404
from django.db.models.base import ObjectDoesNotExist
# Create your views here.
def landing(request):
    pics = Image.get_all()
    areas = Location.get_all()
    categs = Category.get_all()
    return render(request, 'index.html', {"pics": pics, "areas":areas, "categs":categs})
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_imgs = Image.img_searcher(search_term)
        title = f"For {search_term}"

        return render(request, 'search.html', {"title":title, "imgs":searched_imgs})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message}) 
def by_location(request, location):
    title = location
    pics = Image.get_by_loc(location)
    return render(request, "location.html", {"title":title, "pics": pics})           

def photograph(request, photo_id):
    try:
        image = Image.get_by_id(id=photo_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})        
