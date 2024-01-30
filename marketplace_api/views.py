
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .models import Category
from .models import Product
from .serializers import UserProfileSerializer
from .serializers import CategorySerializer
from .serializers import ProductSerializer
from rest_framework import viewsets, permissions

from rest_framework import viewsets

class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username
            

           
            marketplace_api = UserProfile.objects.get(user=user)
            marketplace_api = UserProfileSerializer(marketplace_api)

            return Response({ 'profile': marketplace_api.data, 'username': str(username) })
        except:
            return Response({ 'error': 'Something went wrong when retrieving profile' })

class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            data = self.request.data
            first_name = data['first_name']
            last_name = data['last_name']
            phone = data['phone']
            email = data['email']

            UserProfile.objects.filter(user=user).update(first_name=first_name, last_name=last_name, phone=phone, email=email)

            marketplace_api = UserProfile.objects.get(user=user)
            marketplace_api = UserProfileSerializer(marketplace_api)

            return Response({ 'profile': marketplace_api.data, 'username': str(username) })
        except:
            return Response({ 'error': 'Something went wrong when updating profile' })


class ProductView(viewsets.ModelViewSet):
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = []  
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryView(viewsets.ModelViewSet):
    
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = []  
    queryset=Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']