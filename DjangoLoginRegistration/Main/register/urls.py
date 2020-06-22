from django.urls import path
from .views import RegisterViews

urlpatterns = [
    path('', RegisterViews.as_view())
]
    