from django.urls import path
from . import views

urlpatterns = [
    path('website/', views.website, name='website'),
    path('website/', views.mohit, name='mohit'),
]