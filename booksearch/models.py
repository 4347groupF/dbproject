# booksearch/models.py

from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True, db_column='isbn')
    title = models.CharField(max_length=255, db_column='title')
    pages = models.PositiveIntegerField(db_column='pages')
    cover = models.URLField(db_column='cover')
    auth_list = models.CharField(max_length=255, db_column='auth_list')

    def __str__(self):
        return self.title
