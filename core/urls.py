from django.urls import path, include
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("gallery", views.all_photo, name="photos"),
    path("contact", views.contact, name="contact"),
    path("pricing", views.pricing, name="pricing"),
    path("categories", views.category_list, name="categories"),
    path("category/<slug>", views.categories_detail, name="category_detail"),
    path('create-booking/', views.create_booking, name='create_booking'),
    path("photos/<slug>", views.work_detail, name="work_detail"),
    path("review/<token>/", views.review, name="review"),
    path('submit_review/<str:token>/', views.submit_review, name='submit_review'),
    path('drop-a-review/', views.generate_token_and_redirect, name='generate_token'),
    path("about", views.about, name="about"),
]


