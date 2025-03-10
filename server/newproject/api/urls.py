from django.urls import path
from .views import get_books
from .views import create_book,book_details


urlpatterns=[
    path('books/',get_books,name='get_books'),
    path('create/', create_book, name='create_book'),
    path('details/', book_details, name='book_details'),
]