from django.urls import path
from .views import UsersView


urlpatterns = [
    path('register/', UsersView.as_view()), 
]
