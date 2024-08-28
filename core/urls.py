from django.urls import path, include
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("pricing", views.pricing, name="pricing"),
    path("categories", views.category_list, name="categories"),
    path("category/<slug>", views.categories_detail, name="category_detail"),
    path("photos/<slug>", views.work_detail, name="work_detail"),
    path("about", views.about, name="about"),
]


