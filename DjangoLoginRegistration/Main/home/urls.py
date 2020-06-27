from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:email>/', views.HomeView.as_view(), name="home"),
]
