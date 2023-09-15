from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Author")

    def __str__(self):
        return f"{self.full_name} - {self.id}"

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        ordering = ['id']


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name="Books")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return f"{self.title} - {self.id}"

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['id']


class Readers(models.Model):
    full_name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.full_name} - {self.id}"

    class Meta:
        verbose_name = 'reader'
        verbose_name_plural = 'readers'
        ordering = ['id']


# class BookStorage(models.Model):
class BooksRent(models.Model):
    book = models.ForeignKey(Books, verbose_name='book', on_delete=models.SET_NULL, null=True)
    reader = models.ForeignKey(Readers, verbose_name='reader', on_delete=models.SET_NULL, null=True)
    rented_at = models.DateTimeField(verbose_name='book issue date', auto_now_add=True)
    returned_at = models.DateTimeField(verbose_name='book return date', null=True, blank=True)

    def __str__(self):
        return f"{self.reader.full_name} взял {self.book.title}"

    class Meta:
        verbose_name = 'the book is taken'
        verbose_name_plural = 'the books are taken'
        ordering = ('reader',)
