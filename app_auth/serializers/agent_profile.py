from rest_framework import serializers
from app_auth.models.agent_profile import AgentProfile

class AgentProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'
        extra_kwargs = {
            'email': {'required': False},
            'telegram_account': {'required': False},
        }

    def create(self, validated_data):
        profile = AgentProfile.objects.create(**validated_data)
        return profile

class AgentProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'
        read_only_fields = ('user',)

class AgentProfileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'
