#####################################################################################################

# Home Page
from django.shortcuts import render
def home(request):
    return render(request, 'Book/home.html')

#####################################################################################################


from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def year1(request):
    books = Book.objects.filter(batch='year1')
    context = {'books': books}
    return render(request, 'Book/year1.html', context)

def year2(request):
    books = Book.objects.filter(batch='year2')
    context = {'books': books}
    return render(request, 'Book/year2.html', context)

def year3(request):
    books = Book.objects.filter(batch='year3')
    context = {'books': books}
    return render(request, 'Book/year3.html', context)

def year4(request):
    books = Book.objects.filter(batch='year4')
    context = {'books': books}
    return render(request, 'Book/year4.html', context)

#####################################################################################################

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
        form = BookForm(request.POST, request.FILES)
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

    
    except ObjectDoesNotExist:
        context = {'message': 'الكتاب غير موجود.'}
        return render(request, 'Book/book_not_found.html', context)

#####################################################################################################


def college_links(request):
    links = [
        {'title': 'رابط موقع الجامعة :', 'url': ' http://www1.zu.edu.eg/ServiceDetails.aspx?ID=25'},
        {'title': ' رابط المنصة الرقمية :', 'url': 'http://artstudent.eps.zu.edu.eg/Views/StudentViews/StudentLogin?AspxAutoDetectCookieSupport=1'},
        {'title': ' رابط دخول [بيانات] الطالب :', 'url': ' http://www.militaryeducation.zu.edu.eg/Views/ED_Students/Login/?'},
        {'title': 'رابط الحصول علي الكود : ', 'url': 'http://www.militaryeducation.zu.edu.eg/Views/General/GetStudInfo'},
        {'title': ' رابط إستمارة الكشف الطبي :', 'url': 'http://www.medical4.zustudents.zu.edu.eg/'},
        {'title': 'رابط التربية العسكرية : ', 'url': 'http://www.militaryeducation.zu.edu.eg/Views/ED_Students/StudentMilitary'},
        {'title': 'رابط سداد مصروفات الجامعة  : ', 'url': 'http://www.militaryeducation.zu.edu.eg/Views/ED_Students/StudExpenses'},
        {'title': ' رابط المقررات الدراسية :', 'url': 'http://artstudent.eps.zu.edu.eg/Views/StudentViews/ESubjectsAll'},
        {'title': 'صفحة كلية الآداب الرسمية علي فيسبوك :', 'url': 'https://www.facebook.com/share/16CXmiMcv4/'},
    ]
    context = {'links': links}
    return render(request, 'Book/college_links.html', context)

#####################################################################################################

from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.utils.html import escape

def search_books(request):

    # storage = messages.get_messages(request)
    # storage.used = True
    query = escape(request.GET.get('q', '').strip())
    books = []
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        if not books:
            messages.info(request, 'لا توجد كتب تطابق البحث.')
    else:
        messages.info(request, 'يرجى إدخال استعلام بحث.')
    context = {'books': books, 'query': query}
    return render(request, 'Book/search_books.html', context)
    
# def search_books(request):
#     query = escape(request.GET.get('q', '').strip())
#     books = Book.objects.filter(
#         Q(title__icontains=query) | Q(author__icontains=query)
#         ) if query else Book.objects.all() # list all books
    
#     context = {'books': books, 'query': query}
#     return render(request, 'Book/search_books.html', context)
    
#####################################################################################################
