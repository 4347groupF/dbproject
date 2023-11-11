# booksearch/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # Homepage using index.html template
    path('search/', views.search_books, name='search_books'),  # Search results using book_list.html template
]
