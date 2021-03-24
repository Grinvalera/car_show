from django.http import HttpResponse
from rest_framework import viewsets, permissions, serializers

from .models import Car, Image, User
from .serializers import CarSerializer, UserSerializer


class CarViewSet(viewsets.ModelViewSet):

    def car_view(self, brand):
        car_model = Car.objects.filter(brand=brand)
        print(car_model)
        return car_model

    serializer_class = CarSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


def test(request):
    print(request)
