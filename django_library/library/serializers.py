from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Author, Books, Readers, BooksRent


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = ('title',)


class AuthorDetailSerializer(ModelSerializer):
    books = BooksSerializer(many=True)

    class Meta:
        model = Author
        fields = ('full_name', 'books')


class ReadersSerializer(ModelSerializer):
    class Meta:
        model = Readers
        fields = '__all__'


class ReadersDetailSerializer(ModelSerializer):
    books = StringRelatedField(many=True)

    class Meta:
        model = Readers
        fields = ('full_name', 'books')


class BooksRentSerializer(ModelSerializer):
    class Meta:
        model = BooksRent
        fields = '__all__'