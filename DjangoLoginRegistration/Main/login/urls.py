from django.urls import path
from .views import UserLoginViews 

urlpatterns = [
    # path('', views.login, name="login"),
    path('', UserLoginViews.as_view(), name='login'),

]
    