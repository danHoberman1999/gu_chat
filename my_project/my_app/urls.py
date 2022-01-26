from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_page),
    path('contact/', views.contact_page),
]
