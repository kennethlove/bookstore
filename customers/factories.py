import random

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from . import models

from books.factories import BookFactory

fake = Faker()


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = models.Customer

    name = factory.Faker('name')
    email = factory.Faker('email')
    address = factory.Faker('street_address')
    city = factory.Faker('city')
    state = factory.Faker('state')
    country = factory.Faker('country')
    postal_code = factory.Faker('postalcode')

    @factory.lazy_attribute
    def address_2(self):
        if random.choice([0]*9 + [1]):
            return fake.secondary_address()
        return ''


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = models.Purchase

    customer = factory.SubFactory(CustomerFactory)
    placed_at = factory.Faker('date_time_this_year')

    @factory.post_generation
    def books(self, created, extracted, **kwargs):
        if created:
            books = factory.build_batch(BookFactory, size=random.randint(1, 10))
            for book in books:
                self.books.add(book)
        if extracted:
            for book in extracted:
                self.books.add(book)
