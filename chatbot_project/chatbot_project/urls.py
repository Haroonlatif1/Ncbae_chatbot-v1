# chatbot_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chat/', include('chatbot.urls')),  # Include chatbot app's URLs under /api/chat/
    # other urlpatterns as needed
]
