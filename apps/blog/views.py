from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Content
from .serializers import ContentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import action


class ContentViewSet(viewsets.ModelViewSet):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    









# # USING MIXIN & GENERIC

# class BlogList(generics.ListCreateAPIView,
#                     mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
    
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class CrudBlog(generics.RetrieveUpdateDestroyAPIView,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):

#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




# USING APIview

# class All_content(APIView):

#     def get(self, request):
#         data = Content.objects.all()
#         serializer = ContentSerializer(data , many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ContentSerializer(data= request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Crud_content(APIView):

#     def get_object(self , pk):
#         try:
#             return Content.objects.get(id=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)


#     def get(self, request, pk):
#         obj = self.get_object(pk)
#         serializer = ContentSerializer(obj)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         obj = self.get_object(pk)
#         serializer = ContentSerializer(obj , data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         obj = self.get_object(pk)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






# USING FUNCTION



# @api_view(['GET','POST'])
# def contetn_list(request):
#     if request.method == "GET" : 
#         data = Content.objects.all()
#         serializer = ContentSerializer(data , many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST" :
#         serializer = ContentSerializer(data= request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def content_detail(request,pk):

#     try:
#         obj = Content.objects.get(id=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = ContentSerializer(obj)
#         return Response(serializer.data)
    
#     elif request.method == "PUT" :
#         serializer = ContentSerializer(obj , data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(status= status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == "DELETE" :
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




