from django.urls import path
from app_auth.views.users import CustomUserCreateView, CustomTokenObtainPairView, CustomTokenRefreshView

app_name = 'app_auth'

urlpatterns = [
    path('user-create/', CustomUserCreateView.as_view()),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='custom_token_refresh'),
]
