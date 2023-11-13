# booksearch/models.py

from django.db import models

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=250, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    cover = models.CharField(max_length=100, blank=True, null=True)
    auth_list = models.CharField(max_length=100, blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BOOKS'

    def __str__(self):
        return self.title


class Borrower(models.Model):
    card_id = models.AutoField(primary_key=True)
    ssn = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    new_id = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BORROWERS'

    def __str__(self):
        return self.card_id
