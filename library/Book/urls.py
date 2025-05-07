from django.urls import path
from Book import views
urlpatterns = [
    path('books/', views.books_list, name='books_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/search/', views.search_books, name='search_books'),
]
