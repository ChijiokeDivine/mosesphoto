from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Photo, Booking, PhotoshootSchedule, PhotoMedia

# Register your models here.

class PhotoMediaAdmin(admin.TabularInline):
    model = PhotoMedia

class PhotoAdmin(admin.ModelAdmin):
    inlines = [PhotoMediaAdmin]
    list_display = ['photo_image','name', 'category']

admin.site.unregister(Group)

admin.site.register(Category)
admin.site.register(Photo, PhotoAdmin)  # Register Photo with PhotoAdmin
admin.site.register(Booking)
admin.site.register(PhotoshootSchedule)
