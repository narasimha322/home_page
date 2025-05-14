from django.urls import path
from .views import (
    RegisterView, LoginView, CreateStaffView,
    ChangePasswordView, ResetPasswordView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-staff/', CreateStaffView.as_view(), name='create-staff'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # You may skip this if you already have a custom LoginView
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
