from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я автора")
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"


class Book(models.Model):
    book_name = models.CharField(max_length=255, verbose_name='Назва книжки')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField(verbose_name='Кількість сторінок')

    def __str__(self):
        return f'{self.author.name} - "{self.book_name}"'

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
