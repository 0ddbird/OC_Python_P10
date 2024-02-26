from datetime import date

from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "can_be_contacted",
            "can_data_be_shared",
            "birthdate",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def validate_birthdate(self, value):
        today = date.today()
        age = (
            today.year
            - value.year
            - ((today.month, today.day) < (value.month, value.day))
        )
        if age < 15:
            raise serializers.ValidationError(
                "You need to be at least 15 years old to register."
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            can_be_contacted=validated_data["can_be_contacted"],
            can_data_be_shared=validated_data["can_data_be_shared"],
            birthdate=validated_data["birthdate"],
            password=validated_data["password"],
        )
        return user
