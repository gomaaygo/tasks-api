from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'email', 'password1', 'password2', 'is_active', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at', 'is_active')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 as it's not needed for user creation
        password = validated_data.pop('password1')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class SignInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        try:
            super().validate(attrs)
        except AuthenticationFailed as authentication_failed:
            raise serializers.ValidationError({'message': "Invalid username or password, please try again."}) from authentication_failed

        refresh = self.get_token(self.user)
        token = refresh.access_token

        return {
            'id': self.user.id,
            'name': self.user.name,
            'email': self.user.email,
            'token': str(token),
            'refresh': str(refresh),
        }
