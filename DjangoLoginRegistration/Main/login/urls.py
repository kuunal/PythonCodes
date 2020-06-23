from django.urls import path
# from django.contrib.auth.views import LoginView
from .views import LoginViews 

urlpatterns = [
    # path('', views.login, name="login"),
    path('', LoginViews.as_view(), name='login'),

]
    