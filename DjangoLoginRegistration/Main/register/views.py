from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from django.http import JsonResponse
from .models import RegisterModel
from rest_framework.response import Response
from rest_framework import status

class RegisterViews(APIView):

    def get(self, request):
        return render(request, 'register/register.html')

    def post(self, request):
        queryset = RegisterModel.objects.all()
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            print("Insideeeeeeeeeeeeeeeeeeeeeee")
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
 
   