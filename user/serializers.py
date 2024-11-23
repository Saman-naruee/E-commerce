from .models import User, UserProfile
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'address', 'phone', 'birth_date', 'membership']
        read_only_fields = ['id', 'user', 'membership']
