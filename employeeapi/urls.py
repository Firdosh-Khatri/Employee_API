from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from .views import CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]


