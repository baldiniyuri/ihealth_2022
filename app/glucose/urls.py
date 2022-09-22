from django.urls import path
from .views import GlucoseView


urlpatterns = [
    path('glucose/', GlucoseView.as_view()),
    path('glucose/<int:user_id>/', GlucoseView.as_view())
]