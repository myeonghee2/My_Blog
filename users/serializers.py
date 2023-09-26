from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User
from articles.serializers import ArticleListSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    article_set = ArticleListSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)


    class Meta:
        model = User
        fields =["username", "email", "nickname", "fullname", "date_of_birth", "followings", "followers", "article_set", "like_articles"] 


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
    
class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(write_only=True)
    message = serializers.CharField(read_only=True)