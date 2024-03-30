from .models import Employee
from django.contrib.auth.models import User
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['username'] = instance.user.username
        representation['first_name'] = instance.user.first_name
        representation['last_name'] = instance.user.last_name
        representation['email'] = instance.user.email

        return representation
    