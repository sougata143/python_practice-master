from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=30, default = "ABC")
    isbn = models.CharField(max_length=30, default = "ABC")
    author = models.CharField(max_length=30, default = "ABC")
    publisher = models.CharField(max_length=30, default = "ABC")
    
    def __str__(self):
        return self.book_name