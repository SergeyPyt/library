from rest_framework.generics import ListCreateAPIView
from .serializers import AuthorSerializer, BooksSerializer, ReadersSerializer, BooksRentSerializer
from .models import Author, Books, Readers, BooksRent
from rest_framework import permissions


class BookCreateAPIView(ListCreateAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
    permission_classes = [permissions.AllowAny]


class AuthorCreateAPIView(ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]


class ReadersCreateAPIView(ListCreateAPIView):
    serializer_class = ReadersSerializer
    queryset = Readers.objects.all()
    permission_classes = [permissions.AllowAny]


class BooksRentCreateAPIView(ListCreateAPIView):
    serializer_class = BooksRentSerializer
    queryset = BooksRent.objects.all()
    permission_classes = [permissions.AllowAny]


class BooksReader(ListCreateAPIView):
    serializer_class = BooksSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        books_rent = BooksRent.objects.all()
        queryset = Books.objects.filter(pk__in=books_rent.values("book"))
        return queryset


class BooksOver(ListCreateAPIView):
    serializer_class = BooksSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        books_rent_objects = BooksRent.objects.all()
        all_books = Books.objects.all()
        books_rent = Books.objects.filter(pk__in=books_rent_objects.values("book"))
        queryset = all_books.exclude(pk__in=books_rent.values("id"))
        return queryset


"""
   реализовать систему авторизации(2 формы(авторизация и регистрация и views)
   JWT auth почитать
"""
