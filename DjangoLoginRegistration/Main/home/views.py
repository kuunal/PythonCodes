from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class HomeView(APIView):
    def get(self, request):
        return render(request, 'home/home.html')