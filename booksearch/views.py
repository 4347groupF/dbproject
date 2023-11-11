# booksearch/views.py
from django.db.models import Q
from django.views.generic import ListView
from .models import Book
from django.shortcuts import render
import mysql.connector

# Your existing code for the 'home' view
def home(request):
    return render(request, 'booksearch/index.html', {})

# Existing 'search_results' view
'''
def search_results(request):
    query = request.GET.get('q')
    books = []
    context = {
        'query': query,
        'books': books,
    }
    return render(request, 'booksearch/book_list.html', context)
'''
def search_books(request):
    if request.method == 'GET':
        keyword = request.GET.get('q', '')  # Get the search keyword from the query parameter

        # Database configuration
        config = {
            'user': 'library_admin',
            'password': 'cDavis4347GRP',
            'host': '159.223.135.139',
            'port': '3306',
            'database': 'LibraryProject',
        }

        try:
            conn = mysql.connector.connect(**config)

            if conn.is_connected():
                cursor = conn.cursor()

                # Execute title SQL query
                query = f"SELECT isbn, title, pages, cover, auth_list FROM BOOKS WHERE title LIKE '%{keyword}%'"
                cursor.execute(query)

                # Fetch results
                books = []
                for (isbn, title, pages, cover, auth_list) in cursor:
                    books.append({
                        'isbn': isbn,
                        'title': title,
                        'pages': pages,
                        'cover': cover,
                        'auth_list': auth_list,
                    })
                
                # Execute author SQL query
                query = f"SELECT isbn, title, pages, cover, auth_list FROM BOOKS WHERE auth_list LIKE '%{keyword}%'"
                cursor.execute(query)

                for (isbn, title, pages, cover, auth_list) in cursor:
                    books.append({
                        'isbn': isbn,
                        'title': title,
                        'pages': pages,
                        'cover': cover,
                        'auth_list': auth_list,
                    })

                # Execute ISBN SQL query
                query = f"SELECT isbn, title, pages, cover, auth_list FROM BOOKS WHERE isbn LIKE '%{keyword}%'"
                cursor.execute(query)

                for (isbn, title, pages, cover, auth_list) in cursor:
                    books.append({
                        'isbn': isbn,
                        'title': title,
                        'pages': pages,
                        'cover': cover,
                        'auth_list': auth_list,
                    })

                context = {
                    'query': keyword,
                    'books': books,
                }
                return render(request, 'booksearch/book_list.html', context)

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            # Close cursor and connection
            cursor.close()
            conn.close()

    # Handle other cases or errors here
    return render(request, 'booksearch/book_list.html', {})  # Return an empty context for now

# Updated code for the 'BookListView' class
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'BOOKS'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) |
                Q(auth_list__icontains=query)
            )
        return Book.objects.all()
