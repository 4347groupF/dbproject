# booksearch/views.py
from django.db import models
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'booksearch/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(
                models.Q(isbn__icontains=query) |
                models.Q(title__icontains=query) |
                models.Q(author__icontains=query)
            )
        return Book.objects.all()
