from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response


class RegesitrationApiView(APIView):

    def post(self, request ):
        try:
            serializer = RegistrationSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response("User created successfully ", status=status.HTTP_201_CREATED)
            

            else: 
                return Response("Failed in if case to valid data",status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response("Failed in Try case to get data",status=status.HTTP_400_BAD_REQUEST)
        
