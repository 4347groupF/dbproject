# booksearch/urls.py

from django.urls import path
from .views import BookListView

urlpatterns = [
    path('search/', BookListView.as_view(), name='book-list'),
]
