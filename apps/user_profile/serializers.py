"User & UserProfile serializers"

from rest_framework import serializers

from .models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only = ("id", "user")

class UserSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = "__all__"
        read_only = ("id",)

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        read_only = ("id",)
