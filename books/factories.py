import factory
from factory.django import DjangoModelFactory
import faker

from . import models

fake = faker.Faker()


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = models.Author

    name = factory.Faker('name')


class BookFactory(DjangoModelFactory):
    class Meta:
        model = models.Book

    title = factory.lazy_attribute(lambda n: ' '.join(fake.words(nb=3)).title())
    isbn = factory.Faker('isbn10')
    genre = factory.Iterator([models.POETRY, models.SFF, models.HORROR, models.WAR, models.ROMANCE])
    fiction = factory.Faker('boolean')
    hardback = factory.Faker('boolean')
    in_stock = factory.Faker('boolean')
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    author = factory.SubFactory(AuthorFactory)
