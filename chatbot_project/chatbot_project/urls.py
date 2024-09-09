# chatbot_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chat/', include('chatbot.urls')),    # Add more urlpatterns as needed for other apps or endpoints
]
