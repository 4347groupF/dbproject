# booksearch/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.login_page, name='login_page'),
    path('login/', views.login_validation, name='login_validation'),
    path('index/', views.home, name='index'),
    path('search/', views.search_books, name='search_books'),  # Updated to use search_books view
    path('login_fail/',views.login_page_fail, name='login_page_fail'),
    path('loans/', views.loan_search, name='loan_search'),
    # Define a URL pattern for the 'checkout' view
    path('checkout/<str:isbn>/', views.checkout, name='checkout'),
]