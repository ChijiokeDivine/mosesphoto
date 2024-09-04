from django.shortcuts import render
from .models import Photo, Category
from .models import Booking, Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

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
    categories = Category.objects.all()
    referral_choices = Booking.REFERRAL_CHOICES
    return render(request, "contact.html", {'categories': categories,'referral_choices': referral_choices,})

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


@csrf_exempt
def create_booking(request):
    # Extract form data from the request
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    category_id = request.POST.get('category')  # Assuming category is passed as ID
    heard_about_us = request.POST.get('heard_about_us')
    additional_details = request.POST.get('message', '')  # The message field from the form
    
    # Validate and fetch the category object
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'Invalid category selected.'}, status=400)
    
    # Create a new booking instance
    booking = Booking.objects.create(
        name=name,
        email=email,
        phone_number=phone_number,
        category=category,
        heard_about_us=heard_about_us,
        additional_details=additional_details
    )
    
    # Return a success response
    return JsonResponse({'message': 'Booking successfully created!'})