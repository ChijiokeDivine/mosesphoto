from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Photo, Booking, PhotoshootSchedule, PhotoMedia, Review

# Register your models here.
admin.site.site_header = "Moses.cam Admin"
class PhotoMediaAdmin(admin.TabularInline):
    model = PhotoMedia

class PhotoAdmin(admin.ModelAdmin):
    inlines = [PhotoMediaAdmin]
    list_display = ['photo_image','name', 'category']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name','review']

admin.site.unregister(Group)

admin.site.register(Category)
admin.site.register(Photo, PhotoAdmin)  # Register Photo with PhotoAdmin
admin.site.register(Booking)
admin.site.register(PhotoshootSchedule)
admin.site.register(Review, ReviewAdmin)
