from django.urls import path
from .views import GlucoseView


urlpatterns = [
    path('glucose/<int:user_id>/', GlucoseView.as_view())
]