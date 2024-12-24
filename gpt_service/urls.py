from django.urls import path
from .views import VicunaGenerateView

urlpatterns = [
    path('generate/', VicunaGenerateView.as_view(), name='generate'),
]
