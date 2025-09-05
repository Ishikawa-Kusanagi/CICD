from django.contrib.auth import get_user_model
from django.test import TestCase
from notes.models import Note

User = get_user_model()


class NoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Satoshi_Nakamoto'
        )
        self.note = Note.objects.create(
            user=self.user,
            title='Genesis_block',
            text='1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'
        )

    def test_note_creating(self):
        self.assertEqual(self.note.title, 'Genesis_block')
        self.assertEqual(self.note.text, '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
