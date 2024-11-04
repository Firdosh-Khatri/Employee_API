from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, attrs):
        if not attrs.get('name'):
            raise serializers.ValidationError({'name': 'This field is required.'})
        return attrs
