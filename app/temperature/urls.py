from django.urls import path
from .views import TemperatureView


urlpatterns = [
    path('temperature/', TemperatureView.as_view()),
    path('temperature/<int:user_id>/', TemperatureView.as_view()),
    path('temperature/<int:user_id>/<int:medic_id>/', TemperatureView.as_view()),
]