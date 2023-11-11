# booksearch/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.home, name='index'),
    path('search/', views.search_books, name='search_books'),  # Updated to use search_books view
    # Define a URL pattern for the 'checkout' view
    path('checkout/<str:isbn>/', views.checkout, name='checkout'),
    path('login/', views.login_view, name='login'),
]
