from django.urls import path
from .views import firstFunction


urlpatterns = [
    path('first', firstFunction)
]