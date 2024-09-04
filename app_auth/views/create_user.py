from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from django.core.cache import cache
from app_auth.models.user import CustomUser
from app_auth.serializers.create_user_serializers import CustomUserCreateSerializer
from app_auth.serializers.opt_verification import OTPVerificationSerializer


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer

    @swagger_auto_schema(
        operation_description="Register a new user and send an OTP to their email.",
        responses={
            201: "User created successfully, OTP sent to email.",
            400: "Invalid data provided.",
        },
        request_body=CustomUserCreateSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": "User created successfully, OTP sent to email."},
            status=status.HTTP_201_CREATED
        )


class VerifyOTPView(generics.GenericAPIView):

    @swagger_auto_schema(
        operation_description="Register a new user and OTP Verification",
        request_body=OTPVerificationSerializer,
        responses={
            201: "User created successfully, OTP sent to email.",
            400: "Invalid data provided.",
        }
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if not email or not otp:
            return Response({"error": "Email and OTP are required."}, status=status.HTTP_400_BAD_REQUEST)

        cached_otp = cache.get(f"otp_{email}")

        if cached_otp and str(cached_otp) == otp:
            try:
                user = CustomUser.objects.get(email=email)
                user.is_active = True  # Mark user as active (verified)
                user.save()
                return Response({"message": "OTP verified. User is now active."}, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                user = CustomUser.objects.get(email=email)
                user.is_active = False  # Mark user as active (verified)
                user.save()
                return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        else:
            user = CustomUser.objects.get(email=email)
            user.is_active = False  # Mark user as active (verified)
            user.save()
            return Response({"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)
