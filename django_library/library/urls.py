from django.urls import path
from .endpoints import (BookCreateAPIView, BooksRentCreateAPIView, ReadersCreateAPIView, AuthorDetailListCreateAPIView, ReadersCreateListAPIView)


urlpatterns = [
    path('books/', BookCreateAPIView.as_view()),
    path('reader/', ReadersCreateAPIView.as_view()),
    path('booksrent/', BooksRentCreateAPIView.as_view()),
    path('author/', AuthorDetailListCreateAPIView.as_view()),
    path('readerviews/', ReadersCreateListAPIView.as_view()),
]
