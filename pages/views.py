# mb/pages/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')  # Ensure you have a `home.html` template in the templates directory

def about(request):
    return render(request, 'pages/about.html')