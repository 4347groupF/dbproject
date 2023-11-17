from datetime import datetime

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection
from .models import *

def home(request):
    return render(request, 'booksearch/index.html', {})

def search_books(request):
    if request.method == 'GET':
        keyword = request.GET.get('q', '')  # Get the search keyword from the query parameter
        try:
            with connection.cursor() as cursor:
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

        except Exception as e:
            print(f"Error: {e}")

    # Handle other cases or errors here
    return render(request, 'booksearch/book_list.html', {})

# TODO convert or connect with another function that will render the page
# Currently just returns the JSON response
def loan_search(request):
    if request.method == 'GET':
        keyword = request.GET.get('q', '') 

        loans = []
        for p in BookLoans.objects.raw(
            f"""SELECT first_name, last_name, loan_id, b.card_id, date_out, due_date
            FROM BOOK_LOANS as bl
            INNER JOIN BORROWERS as b
            ON bl.card_id = b.card_id
            WHERE first_name LIKE %(search)s OR last_name LIKE %(search)s OR isbn LIKE %(search)s or b.card_id LIKE %(search)s""",
            {"search": f"%{keyword}%"}
        ):
            loans.append({
                'loan_id': p.loan_id,
                'first_name': p.first_name,
                'last_name': p.last_name,
                'card_id': p.card_id,
                'date_out': p.date_out,
                'due_date': p.due_date,
            })
            
        context = {
            'query': keyword,
            'loans': loans,
        }
        return JsonResponse(context)

# TODO display confirmation page
def checkin(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
        book.available = 0

        loan = BookLoans.objects.get(isbn=isbn, date_in=None)
        loan.date_in = datetime.today().date()

        book.save()
        loan.save()
    except Book.DoesNotExist:
        # TODO show error response
        ...

def checkout(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)

        borrower = Borrower.objects.get(card_id=request.session.get('borrower_id', None))
        if borrower is None:
            # no user is logged in, fail request
            return 
        
        # Check other conditions
        if book.available == 0:
            e = {
                "error_message": f"Sorry, this book has already been checked out and is currently not available. Try again at another time."
            }
            return render(request, 'booksearch/checkout_failure.html', e)
    
        if (c := BookLoans.objects.filter(card=borrower, date_in=None).count()) >= 3:
            e = {
                "error_message": f"Sorry, you have {c} books checked out already. The limit for concurrent checkouts is 3. Please return some books to borrow additional ones."
            }
            return render(request, 'booksearch/checkout_failure.html', e)

        # Passed conditions
        book.available = 0
        book.save()

        loan = BookLoans.objects.create(card=borrower, isbn=book)
        print(loan.loan_id)

        context = {
            'book': book,
            'due_date': loan.due_date
        }
        return render(request, 'booksearch/checkout_confirmation.html', context)
    except Book.DoesNotExist:
        # Handle the case where the book with the given ISBN is not found
        return render(request, 'booksearch/checkout_confirmation.html', {'isbn': isbn})

# views.py
def login_page(request):
    return render(request, "booksearch/login.html", {})

def login_page_fail(request):
    return render(request, "booksearch/login_fail.html", {})

def login_validation(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        try:
            with connection.cursor() as cursor:
                # Execute SQL query
                query = f"SELECT card_id FROM BORROWERS WHERE card_id = '{card_id}'"
                cursor.execute(query)
                borrower = cursor.fetchone()

                if borrower:
                    # Borrower found, proceed with login
                    request.session['borrower_id'] = card_id
                    return redirect('index')
                else:
                    # Borrower not found, return error message
                    return render(request, 'booksearch/login_fail.html', {})

        except Exception as e:
            print(f"Error: {e}")
            # Handle database connection error
            return render(request, 'login.html', {'error_message': 'Database error'})

    return render(request, 'login.html')