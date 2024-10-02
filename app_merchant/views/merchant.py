from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from app_merchant.models.merchant import Merchant
from app_merchant.serializers.merchant import MerchantSerializer, MerchantUpdateSerializer
from services.admin_checker import IsSuperAdmin


class MerchantCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MerchantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MerchantRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request, pk):
        try:
            merchant = Merchant.objects.get(pk=pk)
        except Merchant.DoesNotExist:
            raise NotFound('A merchant with this ID does not exist.')
        serializer = MerchantSerializer(merchant)
        return Response(serializer.data)


class MerchantUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def patch(self, request, pk):
        try:
            merchant = Merchant.objects.get(pk=pk)
        except Merchant.DoesNotExist:
            raise NotFound('A merchant with this ID does not exist.')
        serializer = MerchantUpdateSerializer(merchant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MerchantDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def delete(self, request, pk):
        try:
            merchant = Merchant.objects.get(pk=pk)
        except Merchant.DoesNotExist:
            raise NotFound('A merchant with this ID does not exist.')
        merchant.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
