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


class borrower(models.Model):
    card_id = models.PositiveIntegerField(unique=True, db_column='card_id')
    ssn = models.TextField(db_column='ssn')
    address = models.TextField(db_column='address')
    phone =  models.TextField(db_column='phone')
    id =  models.TextField(db_column='id')
    first_name = models.CharField(max_length=50, db_column='first_name')
    last_name = models.CharField(max_length=50, db_column='last_name')
    email = models.CharField(max_length=50,db_column='email')
    city = models.CharField(max_length=50,db_column='city')
    state = models.CharField(max_length=50, db_column='state')

    def __str__(self):
        return self.card_id
