from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = ['id', 'user', 'department', 'phone', 'role']

    def to_internal_value(self, data):
        principal_data = super().to_internal_value(data) 
        principal_data.update(username=data.get('username', ''), first_name=data.get('first_name', ''), last_name=data.get('last_name', ''), email=data.get('email', ''))
        return principal_data

    def update(self, instance, validated_data):
        related_instance = instance.user
        for attr_name, value in validated_data.items():
            if attr_name in ["username", "first_name", "last_name", "email"] and value:
                setattr(related_instance, attr_name, value)
        related_instance.save()
        return super(EmployeeSerializer,self).update(instance, validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.id
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
    