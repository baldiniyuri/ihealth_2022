from django.urls import path
from .views import UsersView, LoginView, Logout, ProfilePictureView


urlpatterns = [
    path('register/', UsersView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/<int:user_id>/', Logout.as_view()),
    path('profile/picture/', ProfilePictureView.as_view()),
    path('profile/picture/<int:user_id>/', ProfilePictureView.as_view()), 
]
