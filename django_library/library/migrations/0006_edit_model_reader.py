# Generated by Django 4.2.5 on 2023-09-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_edit_model_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['id'], 'verbose_name': 'book', 'verbose_name_plural': 'books'},
        ),
        migrations.RemoveField(
            model_name='readers',
            name='books',
        ),
        migrations.AddField(
            model_name='readers',
            name='books',
            field=models.ManyToManyField(to='library.books'),
        ),
    ]
