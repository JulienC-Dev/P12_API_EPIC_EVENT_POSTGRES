from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from .views import ClientAPIView, EmployeeAPIView, ContractAPIView

router = routers.SimpleRouter()
router.register(r'client', ClientAPIView, basename='client')
router.register(r'employee', EmployeeAPIView, basename='employee')
router.register(r'contract', ContractAPIView, basename='contract')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
]

