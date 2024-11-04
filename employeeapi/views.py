from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        department = request.query_params.get('department', None)
        role = request.query_params.get('role', None)
        page = request.query_params.get('page', 1)
        employees = self.queryset

        if department:
            employees = employees.filter(department=department)
        if role:
            employees = employees.filter(role=role)

        # Implement pagination in the app
        start = (int(page) - 1) * 10
        end = start + 10
        paginated_employees = employees[start:end]
        serializer = self.get_serializer(paginated_employees, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            employee = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

# Create your views here.
