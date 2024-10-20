from django.urls import path
from .views import generate_message

urlpatterns = [
    path('generate/', generate_message, name='generate_message'), 
]