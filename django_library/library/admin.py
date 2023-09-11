from django.contrib import admin
from .models import (Books, Author, Readers, BooksRent)


admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Readers)
admin.site.register(BooksRent)
