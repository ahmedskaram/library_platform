from django.urls import path
from Book import views

app_name = 'Book'

urlpatterns = [
    path('home/', views.home, name='home'),

    path('year1/', views.year1, name='year1'),
    path('year2/', views.year2, name='year2'),
    path('year3/', views.year3, name='year3'),
    path('year4/', views.year4, name='year4'),

    path('books/', views.books_list, name='books_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/search/', views.search_books, name='search_books'),
    path('links/', views.college_links, name='college_links'),
]
