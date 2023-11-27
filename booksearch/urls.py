# booksearch/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Existing URL patterns
    path('', views.login_page, name='login_page'),
    path('login_fail/', views.login_validation, name='login_validation'),
    path('signup/', views.signup, name='signup_page'),
    path('index/', views.home, name='index'),
    path('search/', views.search_books, name='search_books'),  # Updated to use search_books view
    path('loans/', views.loans, name='loan_search'),
    path('fines/', views.fines, name='fines'),
    path('update_fines/', views.update_fines, name='update_fines'),
    path('profile/',views.profile_page, name='profile_page'),
    path('checkout/<str:isbn>/', views.checkout, name='checkout'),
]