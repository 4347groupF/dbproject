# booksearch/models.py
from datetime import datetime, timedelta

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
        return str(self.card_id)

class BookLoans(models.Model):
    loan_id = models.AutoField(primary_key=True)
    isbn = models.ForeignKey(Book, models.DO_NOTHING, db_column='isbn', null=True)
    card = models.ForeignKey(Borrower, models.DO_NOTHING, null=True)
    date_out = models.DateField(default=datetime.today().date())
    due_date = models.DateField(default=datetime.today().date() + timedelta(days=14))
    date_in = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BOOK_LOANS'
    
    def __str__(self):
        return str(self.loan_id)