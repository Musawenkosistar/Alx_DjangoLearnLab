from django.urls import path
from . import views

urlpatterns = [
    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Book views
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # Other book pages
    path('books/', views.list_books, name='list_books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]

