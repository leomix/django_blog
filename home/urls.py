from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    # Example: path('home/', views.home, name='home'),
    path('', views.render_home, name='home'),
]