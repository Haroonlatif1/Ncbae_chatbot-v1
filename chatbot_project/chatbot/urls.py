# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),  # Example endpoint, adjust as per your structure
    # Add more paths as needed for other API endpoints
        path('create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('get_users/', views.GetUsersView.as_view(), name='get_users'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]
