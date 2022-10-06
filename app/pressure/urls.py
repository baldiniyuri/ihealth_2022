from django.urls import path
from .views import BloodPressureView


urlpatterns = [
    path('pressure/<int:user_id>/', BloodPressureView.as_view()),
]