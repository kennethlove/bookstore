from django.db import models

POETRY = 'poetry'
SFF = 'sff'
HORROR = 'horror'
WAR = 'war'
ROMANCE = 'romance'


class Book(models.Model):
    GENRES = [
        (POETRY, 'Poetry'),
        (SFF, 'Science Fiction/Fantasy'),
        (HORROR, 'Horror'),
        (WAR, 'War'),
        (ROMANCE, 'Romance'),
    ]
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30)
    genre = models.CharField(max_length=15, choices=GENRES, default='', blank=True)
    fiction = models.BooleanField(default=True)
    author = models.ForeignKey('Author', related_name='books')
    hardback = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    in_stock = models.BooleanField(default=True)

    class Meta:
        unique_together = ['hardback', 'title', 'author']

    def __str__(self):
        return f'{self.title} by {self.author.name}'


class Author(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
