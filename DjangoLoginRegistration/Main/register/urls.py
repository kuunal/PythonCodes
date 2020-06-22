from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterViews.as_view(), name="register"),
    path('<str:token>/<str:email>', views.verify_user, name="verify")
]
    