from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('<str:email>/', views.HomeView.as_view(), name="home"),
]
