from django.shortcuts import render
from .models import Image, Location, Category
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
        message = f"For {search_term}"

        return render(request, 'search.html', {"term":term, "imgs":searched_imgs})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message}) 
def by_location(request, location):
    area = location
    pics = Image.get_by_loc(location)
    return render(request, "by-location.html", {"area":area, "pics": pics})            