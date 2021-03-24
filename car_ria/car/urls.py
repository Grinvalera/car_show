from django.urls import path
from rest_framework import routers

from .views import CarViewSet, UserViewSet, test

router = routers.DefaultRouter()
router.register(r'car/<str:brand>', CarViewSet, basename='CarView')
router.register(r'user', UserViewSet)

urlpatterns = router.urls+[
    path('car/', test)
]
