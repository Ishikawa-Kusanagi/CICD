from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class NoteStatus(models.TextChoices):
    'Статусы Заметок'

    DRAFT = 'DRAFT', _('Черновик')
    OPEN = 'OPEN', _('Опубликован')
    CLOSED = 'CLOSED', _('Закрыт')


class Note(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name=_('Пользователь')
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('Заголовок')
    )
    text = models.TextField(
        verbose_name=_('Текст заметки')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата обновления')
    )
    status = models.CharField(
        max_length=10,
        choices=NoteStatus.choices,
        default=NoteStatus.OPEN,
        verbose_name=_('Статус')
    )

    def __str__(self):
        return f'{self.title} от {self.user} ({self.status})'

    class Meta:
        verbose_name = _('Заметка')
        verbose_name_plural = _('Заметки')
        ordering = ['-created_at']
        permissions = [
            ('view_draft', 'Can view draft notes'),  # Дополнительные права
        ]
