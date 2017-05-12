from django.test import TestCase

from . import factories
from . import models


class BookTests(TestCase):
    def test_book_creation(self):
        book = factories.BookFactory()
        self.assertIn(book.author.name, str(book))
