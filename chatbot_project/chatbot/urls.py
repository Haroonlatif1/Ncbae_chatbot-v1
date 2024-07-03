# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),  # Example endpoint, adjust as per your structure
    # Add more paths as needed for other API endpoints
]
