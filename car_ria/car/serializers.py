from rest_framework import serializers, permissions

from .models import Car, Image, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['_password', '_remember_password']


class CarSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ('__all__')