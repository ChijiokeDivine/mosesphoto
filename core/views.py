from django.shortcuts import render
from .models import Photo, Category
# Create your views here.
def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def pricing(request):
    return render(request, "pricing.html")

def categories_detail(request, slug):
    category = Category.objects.get(slug=slug)
    photos = Photo.objects.filter( category=category)
    context = {
        'category': category,
        'photos': photos
    }
    return render(request, "work.html", context)

def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, "photography.html")

def work_detail(request, slug):
    photo = Photo.objects.get(slug=slug)
    recommended_photos = Photo.objects.filter(category=photo.category).order_by("?")[:2]
    context = {
        'photo': photo,
        're_photo': recommended_photos,
    }
    return render(request, "work-detail-1.html", context)

