from rest_framework import serializers
from .models import AgentProfile

class AgentProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['user', 'full_name', 'email', 'nid_number', 'telegram_account']

    def create(self, validated_data):
        return AgentProfile.objects.create(**validated_data)


class AgentProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['id', 'full_name', 'email', 'nid_number', 'is_active', 'telegram_account']

        extra_kwargs = {
            'id': {'read_only': True}
        }

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email = validated_data.get('email', instance.email)
        instance.nid_number = validated_data.get('nid_number', instance.nid_number)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.telegram_account = validated_data.get('telegram_account', instance.telegram_account)
        instance.save()
        return instance


class AgentProfileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['id', 'user', 'full_name', 'email', 'nid_number', 'is_active', 'telegram_account', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

