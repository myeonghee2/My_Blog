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