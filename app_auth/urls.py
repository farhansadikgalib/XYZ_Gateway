from django.urls import path

from app_auth.views.create_user import VerifyOTPView, CustomUserCreateView
from app_auth.views.users import CustomTokenObtainPairView, CustomTokenRefreshView

app_name = 'app_auth'

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='user-register'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='custom_token_refresh'),
]
