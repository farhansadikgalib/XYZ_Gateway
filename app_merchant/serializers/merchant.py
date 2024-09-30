from rest_framework import serializers
from app_merchant.models.merchant import Merchant

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = [
            'user',
            'name',
            'email',
            'contact_number',
            'api_key',
            'secret_key',
            'is_active',
            'registration_date',
        ]

