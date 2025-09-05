from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['user'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name', ''],
            last_name=validated_data['last_name', '']
        )
        return user
