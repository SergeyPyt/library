from rest_framework.serializers import ModelSerializer
from .models import Author, Books, Readers, BooksRent


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class ReadersSerializer(ModelSerializer):
    class Meta:
        model = Readers
        fields = '__all__'


class BooksRentSerializer(ModelSerializer):
    class Meta:
        model = BooksRent
        fields = '__all__'
