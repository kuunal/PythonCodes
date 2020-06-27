from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('', views.HomeView.as_view(), name="home"),
]
