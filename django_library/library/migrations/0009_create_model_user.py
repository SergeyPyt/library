# Generated by Django 4.2.5 on 2023-09-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_books_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksrent',
            name='rented_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='book issue date'),
        ),
    ]
