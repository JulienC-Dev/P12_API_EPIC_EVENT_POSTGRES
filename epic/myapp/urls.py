from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from .views import ClientAPIView, EmployeeAPIView

router = routers.SimpleRouter()
router.register(r'client', ClientAPIView, basename='client')
router.register(r'employee', EmployeeAPIView, basename='employee')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
]

