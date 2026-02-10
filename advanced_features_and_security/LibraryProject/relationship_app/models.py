from django.conf import settings 
from django.db import models 
from django.db.models.signals import post_save 
from django.dispatch import receiver

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
            ("can_view", "Can view book"),
        ]

    def __str__(self):
        return self.title

# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)  # ✅ Book is now defined
    def __str__(self):
        return self.name
