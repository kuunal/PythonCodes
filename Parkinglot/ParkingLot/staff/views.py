from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from rest_framework.response import Response

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        print(request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            # serializer.save()
            return Response(200)
        return Response(400)