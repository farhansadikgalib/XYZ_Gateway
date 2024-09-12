from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_auth.models.agent_profile import AgentProfile
from app_auth.serializers.agent_profile import (
    AgentProfileCreateSerializer,
    AgentProfileUpdateSerializer,
    AgentProfileRetrieveSerializer,
)
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# APIView to handle the creation of AgentProfile
class AgentProfileCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema('Create Agent Profile', request_body=AgentProfileCreateSerializer)
    def post(self, request, *args, **kwargs):
        serializer = AgentProfileCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# APIView to handle retrieving a single AgentProfile by its ID
class AgentProfileRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Profile Get")
    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(AgentProfile, pk=pk)
        serializer = AgentProfileRetrieveSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


# APIView to handle updating an existing AgentProfile
class AgentProfileUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(AgentProfile, pk=pk)
        serializer = AgentProfileUpdateSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(AgentProfile, pk=pk)
        serializer = AgentProfileUpdateSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
