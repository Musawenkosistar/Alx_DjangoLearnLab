from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
]

urlpatterns += [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]

urlpatterns += [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
