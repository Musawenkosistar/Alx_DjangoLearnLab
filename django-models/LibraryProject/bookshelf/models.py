from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bookshelf_profile')
    role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])

    def __str__(self):
        return f"{self.user.username} - {self.role}"
