from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image, Category, Location
# Create your views here.
def index(request):
    # get all images ordered by the most recent
    images = Image.objects.all().order_by('-id')
    # images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Tribal Gallery'
    return render(request, 'index.html', {'images': images, 'locations': locations, 'categories': categories, 'title': title})

def search(request):
    title = 'Search'
    categories = Category.objects.all()
    # locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category').lower()
        found_results = Image.filter_by_category(search_term)
        message = f"{search_term}"
        locations = Location.objects.all()

        return render(request, 'search.html',{'message': message,'images': found_results, "locations":locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html',{"message": message})
    
def location(request, location_id):
    locations = Location.objects.all()
    images = Image.objects.filter(location_id=location_id)
    # get the location name
    location = Location.objects.get(id=location_id)
    title = location
    return render(request, 'location.html', {'images': images, 'locations': locations, 'title': title})