from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    address_2 = models.TextField(blank=True, default='')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, related_name='purchases')
    books = models.ManyToManyField('books.Book', related_name='purchases')
    placed_at = models.DateTimeField(default=timezone.now)

    @property
    def total(self):
        return sum(self.books.values_list('price', flat=True))
