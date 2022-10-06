from django.urls import path
from .views import GlucoseView, GlucoseMedicView


urlpatterns = [
    path('glucose/', GlucoseView.as_view()),
    path('glucose/<int:user_id>/', GlucoseView.as_view()),
    path('medic-glucose/<int:user_id>/<int:medic_id>/', GlucoseMedicView.as_view())
]