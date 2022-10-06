from django.urls import path
from .views import BloodPressureView,  PressureMedicView


urlpatterns = [
    path('pressure/', BloodPressureView.as_view()),
    path('pressure/<int:user_id>/', BloodPressureView.as_view()),
    path('pressure/<int:user_id>/<int:medic_id>/', PressureMedicView.as_view()),
]