from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterViews.as_view(), name="register"),
    path('<str:email>/<str:token>', views.verify_user, name="verify"),  
    path("check/", views.check_login, name="check")
]
    