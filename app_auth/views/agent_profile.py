from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from app_auth.models.agent_profile import AgentProfile
from app_auth.serializers.agent_profile import (
    AgentProfileCreateSerializer,
    AgentProfileUpdateSerializer,
    AgentProfileRetrieveSerializer
)
from drf_yasg.utils import swagger_auto_schema

# Create API View
class AgentProfileCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=AgentProfileCreateSerializer)
    def post(self, request, *args, **kwargs):
        serializer = AgentProfileCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve API View
class AgentProfileRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve an Agent Profile")
    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(AgentProfile, pk=pk)
        serializer = AgentProfileRetrieveSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Update API View
class AgentProfileUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(AgentProfile, pk=pk)
        serializer = AgentProfileUpdateSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
