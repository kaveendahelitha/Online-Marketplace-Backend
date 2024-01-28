#djoser.serializers import UserCreateSerializer
#django.contrib.auth import get_user_model
#
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'#('id', 'username', )