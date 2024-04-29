from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['user', 'department', 'phone']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.role == 'CO':
            role = 'Courier'
        elif instance.role == 'SA':
            role = 'Admin'
        representation['role'] = role
        representation['username'] = instance.user.username
        representation['first_name'] = instance.user.first_name
        representation['last_name'] = instance.user.last_name
        representation['email'] = instance.user.email

        return representation
    