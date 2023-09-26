from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_date):
        user = super().create(validated_date)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self, validated_date):
        user = super().create(validated_date)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token    
    
# class LogoutSerializer(serializers.Serializer):
#     refresh_token = serializers.CharField(write_only=True)
#     message = serializers.CharField(read_only=True)