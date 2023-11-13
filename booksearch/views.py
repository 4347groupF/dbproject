from django.shortcuts import render, redirect
from .models import Book
from .models import Borrower
import mysql.connector

def home(request):
    return render(request, 'booksearch/index.html', {})

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

                # Execute title / isbn / author SQL query
                query = f"""SELECT isbn, title, pages, cover, auth_list, available
                            FROM BOOKS 
                            WHERE title LIKE %(search)s OR isbn LIKE %(search)s or auth_list LIKE %(search)s"""
                cursor.execute(query, {"search": f"%{keyword}%"})

                # Fetch results
                books = []
                for (isbn, title, pages, cover, auth_list, available) in cursor:
                    books.append({
                        'isbn': isbn,
                        'title': title,
                        'pages': pages,
                        'cover': cover,
                        'auth_list': auth_list,
                        'available': bool(available),
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
    return render(request, 'booksearch/book_list.html', {})

def loan_search():
    pass

def checkout(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
        context = {
            'book': book,
        }
        return render(request, 'booksearch/checkout_confirmation.html', context)
    except Book.DoesNotExist:
        # Handle the case where the book with the given ISBN is not found
        return render(request, 'booksearch/checkout_confirmation.html', {'isbn': isbn})


# views.py

def login(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')

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
            cursor = conn.cursor()

            # Execute SQL query
            query = f"SELECT card_id FROM borrower WHERE card_id = '{card_id}'"
            cursor.execute(query)
            borrower = cursor.fetchone()

            if borrower:
                # Borrower found, proceed with login
                request.session['borrower_id'] = card_id
                return redirect('index')
            else:
                # Borrower not found, return error message
                return render(request, 'login.html', {'error_message': 'Invalid Card ID'})

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            # Handle database connection error
            return render(request, 'login.html', {'error_message': 'Database error'})

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    return render(request, 'login.html')
