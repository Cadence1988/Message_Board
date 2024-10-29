# mb/pages/urls.py
from django.urls import path
from . import views  # Ensure views.py exists in the pages app for any referenced view functions

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home view
    path('about/', views.about, name='about'),
]
