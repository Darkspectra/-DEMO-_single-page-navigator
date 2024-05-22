
from django.urls import path, include
from navigation import views

urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact),
]
