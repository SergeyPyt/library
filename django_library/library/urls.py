from django.urls import path
from .endpoints import (BookCreateAPIView, BooksRentCreateAPIView, ReadersCreateAPIView, AuthorCreateAPIView, BooksReader, BooksOver)


urlpatterns = [
    path('books/', BookCreateAPIView.as_view()),
    path('reader/', ReadersCreateAPIView.as_view()),
    path('booksrent/', BooksRentCreateAPIView.as_view()),
    path('author/', AuthorCreateAPIView.as_view()),
    path('booksreader/', BooksReader.as_view()),
    path('booksover/', BooksOver.as_view()),
]
