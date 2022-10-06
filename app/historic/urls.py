from django.urls import path
from .views import HistoricView


urlpatterns = [
    path('historic/<int:user_id>/', HistoricView.as_view()),
]