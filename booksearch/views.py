from datetime import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection
from .models import *
from .forms import *

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
def checkin(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
        book.available = 0

        loan = BookLoans.objects.get(isbn=isbn, date_in = None)
        loan.date_in = datetime.today().date()

        book.save()
        loan.save()
    except Book.DoesNotExist:
        #show error messsage
        ...



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

def signup_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            borrower = Borrower(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                ssn=form.cleaned_data["ssn"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
                address=form.cleaned_data["address"],
                state=form.cleaned_data["state"],
                city=form.cleaned_data["city"]
            )
            borrower.save()
            print(f"inserted successfully, id {borrower.card_id}")
            return render(request, "booksearch/signup_success.html", {"id": borrower.card_id})
    else:
        form = SignUpForm()
    return render(request, "booksearch/signup.html", {"form": form})


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

def profile_page(request):
    card_id = request.session.get('borrower_id')
    if card_id:
        user = Borrower.objects.get(card_id=card_id)
        book_loans = BookLoans.objects.filter(card_id=card_id)
        context = {
            'user_data': {
                'borrower_id': user.card_id,
                'fines': [],
                'checked_out_books': book_loans,
            }
        }
        return render(request, 'booksearch/profile.html', context)
    return render(request, 'booksearch/login.html')