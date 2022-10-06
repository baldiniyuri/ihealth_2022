from django.urls import path
from .views import BloodPressureView


urlpatterns = [
    path('pressure/', BloodPressureView.as_view()),
    path('pressure/<int:user_id>/', BloodPressureView.as_view()),
]