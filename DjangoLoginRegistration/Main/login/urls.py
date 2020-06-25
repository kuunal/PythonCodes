from django.urls import path
from .views import UserLoginViews 
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.login, name="login"),
    path('', UserLoginViews.as_view(), name='login'),
    path('default', auth_views.LoginView.as_view(), name="log")

]
    