from django.shortcuts import render
from .models import Book

def books_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'Book/books_list.html', context)

#####################################################################################################

from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'Book/add_book.html', context)

#####################################################################################################

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Book

def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        context = {'book': book}
        return render(request, 'Book/book_detail.html', context)
    except ObjectDoesNotExist:
        context = {'message': 'الكتاب غير موجود.'}
        return render(request, 'Book/book_not_found.html', context)

#####################################################################################################

from .models import Book
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist

def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        if request.method == 'POST':
            book.delete()
            return redirect('books_list')
        context = {'book': book}
        return render(request, 'Book/delete_book.html', context)
    
    except ObjectDoesNotExist:
        context = {'message': 'الكتاب غير موجود.'}
        return render(request, 'Book/book_not_found.html', context)

#####################################################################################################

from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.utils.html import escape

def search_books(request):
    query = escape(request.GET.get('q', '').strip())
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
        ) if query else Book.objects.all()
    messages.info(request, 'No books match your search.')
    context = {'books': books, 'query': query}
    return render(request, 'Book/search_books.html', context)

#####################################################################################################

# from django.shortcuts import render
# from django.db.models import Q
# from django.contrib import messages
# from django.utils.html import escape
# from django.core.paginator import Paginator

# def search_books(request):
#     query = escape(request.GET.get('q', '').strip())
#     books = Book.objects.filter(
#         Q(title__icontains=query) | Q(author__icontains=query)
#         ) if query else Book.objects.all()

#     if query and not books:
#         messages.info(request, 'There are no books that match your search.')

# # Add pagination
#     paginator = Paginator(books, 10)  # 10 books per page
#     page_number = request.GET.get('page')  # Page number from the request
#     page_obj = paginator.get_page(page_number)  # Page object
#     context = {'page_obj': page_obj, 'query': query}
#     return render(request, 'search_books.html', context)


#####################################################################################################
