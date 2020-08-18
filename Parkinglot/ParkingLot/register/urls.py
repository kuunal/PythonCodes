from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterViews.as_view(), name="register"),
    path('<str:token>', views.verify_user),  
    path('users/', views.RegisterListView.as_view()),
]
    