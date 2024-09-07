from django.shortcuts import render
from .models import Photo, Category, PhotoMedia
from .models import Booking, Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .utils import alert_owner, booking_confirmed_email
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
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, "pricing.html", context)

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
    return render(request, "categories.html", context)

def work_detail(request, slug):
    photo = Photo.objects.get(slug=slug)
    p_images = photo.p_media.all()
    recommended_photos = Photo.objects.filter(category=photo.category).exclude(id=photo.id).order_by("?")[:4]
    context = {
        'photo': photo,
        'p_images': p_images,
        're_photo': recommended_photos,
    }
    return render(request, "work-detail-1.html", context)


@csrf_exempt
def create_booking(request):
    if request.method == 'POST':
        # Extract form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
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
        alert_owner(
            name=name,
            email=email,
            phone_number=phone_number,
            category=category,
            heard_about_us=heard_about_us,
            additional_details=additional_details
        )
        booking_confirmed_email(name=name,email=email)
        # Return a success response
        return JsonResponse({'message': 'Booking successfully created!'})

    # Handle non-POST requests
    return JsonResponse({'message': 'Invalid request method.'}, status=405)


def all_photo(request):
    photos = Photo.objects.all()
    context = {
        "photos": photos
    }
    return render(request, "photography.html", context)