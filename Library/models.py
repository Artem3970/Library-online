from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    content = models.TextField()
    publication_year = models.IntegerField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.book_name
