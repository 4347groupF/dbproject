# booksearch/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.login_page, name='login_page'),
    path('index/', views.home, name='index'),
    path('login/', views.login_validation, name='login_validation'),
    path('login_fail/',views.login_page_fail, name='login_page_fail'),
    path('signup/',views.signup, name='signup'),
    path('search/', views.search_books, name='search_books'),  
    path('loans/', views.loan_search, name='loan_search'),
    # Define a URL pattern for the 'checkout' view
    path('checkout/<str:isbn>/', views.checkout, name='checkout'),
    path('checkin/<str:isbn>/', views.checkin, name='checkin'),
]