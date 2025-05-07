from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import User
from rest_framework.permissions import  IsAuthenticated,IsAdminUser
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {'refresh': str(refresh), 'access': str(refresh.access_token)}

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'msg': 'User registered successfully'}, status=201)
        return Response(serializer.errors, status=400)

class CreateStaffView(APIView):
    permission_classes = [IsAdminUser]  # Only superuser/staff can create staff

    def post(self, request):
        serializer = StaffCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Staff created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            tokens = get_tokens_for_user(user)
            return Response(tokens, status=200)
        return Response(serializer.errors, status=400)

class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not request.user.check_password(serializer.validated_data['old_password']):
                return Response({'error': 'Wrong old password'}, status=400)
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            return Response({'msg': 'Password changed successfully'})
        return Response(serializer.errors, status=400)

class ResetPasswordView(APIView):
    def put(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            identifier = serializer.validated_data['email_or_phone']
            user = User.objects.filter(email=identifier).first() or User.objects.filter(phone=identifier).first()
            if user:
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({'msg': 'Password reset successful'})
            return Response({'error': 'User not found'}, status=404)
        return Response(serializer.errors, status=400)
