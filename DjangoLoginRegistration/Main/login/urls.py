from django.urls import path
from .views import UserLoginViews 
from django.contrib.auth import views as auth_views
from register.views import check_login

urlpatterns = [
    path('', UserLoginViews.as_view(), name='login'),
    path('check/', check_login),
]
    