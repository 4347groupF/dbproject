# booksearch/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.login_page, name='login_page'),
    path('login_fail/', views.login_validation, name='login_validation'),
    path('signup/', views.signup_page, name='signup_page'),
    path('index/', views.home, name='index'),
    path('search/', views.search_books, name='search_books'),  
    path('loans/', views.loans, name='loan_search'),
    # Define a URL pattern for the 'checkout' view
    path('profile/',views.profile_page, name='profile_page'),
    path('checkout/<str:isbn>/', views.checkout, name='checkout'),
]