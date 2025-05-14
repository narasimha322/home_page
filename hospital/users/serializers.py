from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
import re

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'phone', 'username', 'password1','password2']

    def validate_password(self, value):

        
       
        if len(value) < 8 or len(value) > 15:
            raise serializers.ValidationError("Password must be 8-15 characters long.")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Password must contain at least one number.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("Password must contain at least one special character.")

        return value
    
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password1')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class StaffcreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only = True, style={'input_type' : 'password'})
    password2 = serializers.CharField(write_only = True, style={'input_type' : 'password'})

    class Meta:
        model = User
        fields = ['username' , 'email', 'phone ', 'password1', 'password2']
    
    def validate_password1(self,value):
        if len(value) < 8 or len(value) > 15:
            raise serializers.ValidationError("Password must be 8 - 15 characters long ")
        
        if not re.search(r'[A-Z]',value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'\d',value):
            raise serializers.ValidationError("Password must contain at least one number.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("Password must contain at least one special character.")

        return value
    
    def validate1(self, attrs):
        if atts[password1] != attrs[password2]:
            raise serializers.ValidationError({"password2": "Passwords do not match."})
        return attrs
    
    def cretae(self , validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password1')
        validated_data[is_staff] = True
        validated_data[is_active] = True
        user=User.objects.create_staffuser(**validated_data)
        user.set_password(password)
        user.save()
        return user



class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        identifier = data.get('identifier')
        password = data.get('password')

        user = User.objects.filter(email=identifier).first() or User.objects.filter(phone=identifier).first()
        if user and user.check_password(password):
            return user
        raise serializers.ValidationError("Invalid credentials")

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

class ResetPasswordSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField()
    new_password = serializers.CharField()
