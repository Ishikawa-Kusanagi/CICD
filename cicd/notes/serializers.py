from rest_framework import serializers
from .models import Note
from users.serializers import UserSerializer


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        note = Note.objects.create(
            user=user,
            title=validated_data['title'],
            text=validated_data['text'],
            status=validated_data('status', Note.OPEN)
        )
        return note
