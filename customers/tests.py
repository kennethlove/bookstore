from django.test import TestCase

from . import factories


class PurchaseTests(TestCase):
    def test_basic_purchase(self):
        purchase = factories.PurchaseFactory()
        self.assertGreater(purchase.books.count(), 0)

    def test_total(self):
        purchase = factories.PurchaseFactory()
        total = 0
        for book in purchase.books.all():
            total += book.price
        self.assertEqual(purchase.total, total)
