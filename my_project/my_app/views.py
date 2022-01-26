from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "chatroom.html")

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")