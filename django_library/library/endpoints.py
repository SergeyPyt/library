from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import AuthorSerializer, BooksSerializer,AuthorDetailSerializer, ReadersSerializer, ReadersDetailSerializer, BooksRentSerializer
from .models import Author, Books, Readers, BooksRent
from rest_framework import permissions


class BookCreateAPIView(ListCreateAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
    permission_classes = [permissions.AllowAny]


class AuthorDetailListCreateAPIView(ListCreateAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]


class AuthorCreateAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]


class ReadersCreateAPIView(ListAPIView):
    serializer_class = ReadersSerializer
    queryset = Readers.objects.all()
    permission_classes = [permissions.AllowAny]


class ReadersCreateListAPIView(ListAPIView):
    serializer_class = ReadersDetailSerializer
    queryset = Readers.objects.all()
    permission_classes = [permissions.AllowAny]


class BooksRentCreateAPIView(ListAPIView):
    serializer_class = BooksRentSerializer
    queryset = BooksRent.objects.all()
    permission_classes = [permissions.AllowAny]
