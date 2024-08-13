from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Photo, Booking, PhotoshootSchedule
# Register your models here.


admin.site.unregister(Group)

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Booking)
admin.site.register(PhotoshootSchedule)
