from rest_framework import viewsets, permissions, status
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        # Разрешаем создание пользователя без авторизации
        if self.action == 'create':
            return [permissions.AllowAny()]
        # Для остальных действий нужна авторизация
        return [permissions.IsAuthenticated()]
