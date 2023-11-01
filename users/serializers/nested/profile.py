from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models.profile import Profile

User = get_user_model()


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'telegram_id',
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'telegram_id',
        )
