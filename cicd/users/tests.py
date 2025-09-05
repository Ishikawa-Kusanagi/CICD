# users/tests/test_models.py
from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):
    def test_create_user(self):
        # Создаем нового пользователя
        user = User.objects.create(
            first_name='Иван',
            last_name='Иванов',
            email='ivan@example.com'
        )

        # Проверяем корректность создания
        self.assertEqual(user.first_name, 'Иван')
        self.assertEqual(user.last_name, 'Иванов')
        self.assertEqual(user.email, 'ivan@example.com')
        self.assertEqual(str(user), 'Иван, Иванов')

    def test_unique_email(self):
        # Создаем первого пользователя
        User.objects.create(
            first_name='Петр',
            last_name='Петров',
            email='petr@example.com'
        )

        # Проверяем, что нельзя создать пользователя с тем же email
        with self.assertRaises(Exception):
            User.objects.create(
                first_name='Сидор',
                last_name='Сидоров',
                email='petr@example.com'
            )

    # def test_required_fields(self):
    #     # Проверяем обязательные поля
    #     with self.assertRaises(ValueError):
    #         User.objects.create(
    #             first_name='',
    #             last_name='Иванов',
    #             email='ivan@example.com'
    #         )
    #
    #     with self.assertRaises(ValueError):
    #         User.objects.create(
    #             first_name='Иван',
    #             last_name='',
    #             email='ivan@example.com'
    #         )
    #
    #     with self.assertRaises(ValueError):
    #         User.objects.create(
    #             first_name='Иван',
    #             last_name='Иванов',
    #             email=''
    #         )

    def test_ordering(self):
        # Создаем пользователей с разными фамилиями
        User.objects.create(
            first_name='Анна',
            last_name='Васильева',
            email='anna@example.com'
        )
        User.objects.create(
            first_name='Борис',
            last_name='Алексеев',
            email='boris@example.com'
        )

