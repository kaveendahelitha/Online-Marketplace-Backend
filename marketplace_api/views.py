
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer


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