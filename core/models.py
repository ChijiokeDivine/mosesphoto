from django.db import models
from django.utils.html import mark_safe
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import cloudinary
import requests
from cloudinary.models import CloudinaryField
import pytz
from django.core.exceptions import ValidationError
from django.utils.text import slugify


cloudinary.config( 
  cloud_name = getattr(settings, 'CLOUD_NAME_SECRET', None), 
  api_key = getattr(settings, 'API_KEY', None), 
  api_secret = getattr(settings, 'API_SECRET', None)
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField(folder="category-images")
    starts_from = models.DecimalField(max_digits=10, decimal_places=2, default="99")
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    def url(self):
        return f"/category/{self.slug}"
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it hasn't been set
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Categories"

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pictures')
    name = models.CharField(max_length=100)
    image = CloudinaryField(folder="photos")
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"Picture for {self.name}"
    def url(self):
        return f"/photos/{self.slug}"
    def photo_image(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it hasn't been set
            self.slug = slugify(self.name)
        super(Photo, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Photos"
    
class PhotoMedia(models.Model):
    images = CloudinaryField('media', folder="media", resource_type='auto')
    photo = models.ForeignKey(Photo, related_name="p_media", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo.name  # Assuming Photo has a 'name' attribute
    
    def save(self, *args, **kwargs):
        if self.images and isinstance(self.images.file, InMemoryUploadedFile):
            img = Image.open(self.images.file)

            # Resize the image to the desired dimensions (280x320)
            img = img.resize((280, 320), Image.ANTIALIAS)

            # Save the resized image to a BytesIO object
            output = BytesIO()
            img.save(output, format='WEBP', quality=98)
            output.seek(0)

            # Update the image field with the resized image
            self.images = InMemoryUploadedFile(
                output, 'ImageField',
                f"{self.images.name.split('.')[0]}.webp", 
                'image/webp',
                output.getbuffer().nbytes,
                None
            )
        
        # Call the original save method to save the model instance
        super(PhotoMedia, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Delete the image from Cloudinary before deleting the Blog object
        if self.images:
            # Get the public ID of the image from Cloudinary
            public_id = self.images.public_id
            # Delete the image from Cloudinary
            cloudinary.uploader.destroy(public_id)
        # Call the parent class delete method to delete the Blog object
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Photo medias"

class Booking(models.Model):
    REFERRAL_CHOICES = [
        ('google_search', 'Google Search'),
        ('instagram', 'Instagram'),
        ('recommendation', 'Recommendation'),
        ('blog', 'Blog'),
        ('social_media', 'Social Media'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    additional_details = models.TextField(blank=True, null=True)
    heard_about_us = models.CharField(max_length=50,choices=REFERRAL_CHOICES,default='other',)
    date_created = models.DateTimeField(auto_now_add=True)
    def format_booking_info(self):
        # Define the Berlin timezone
        berlin_tz = pytz.timezone('Europe/Berlin')

        # Convert UTC time to Berlin time
        berlin_time = self.date_created.astimezone(berlin_tz)

        # Format the datetime object as a readable string
        formatted_date = berlin_time.strftime('%d %B %Y, %H:%M %p')  

        return f"Booking by {self.name} for {self.category} on {formatted_date}"
    def __str__(self):
        return self.format_booking_info()


class PhotoshootSchedule(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    date_scheduled = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Photoshoot for {self.booking.name} on {self.date_scheduled}"
    def clean(self):
        # Check if another photoshoot is scheduled for the same date and time
        if PhotoshootSchedule.objects.filter(date_scheduled=self.date_scheduled).exists():
            raise ValidationError(f"A photoshoot is already scheduled for {self.date_scheduled}.")
        
    def save(self, *args, **kwargs):
        # Call the clean method to perform validation before saving
        self.clean()
        super().save(*args, **kwargs)



