from django.contrib.auth.decorators import user_passes_test

def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def check_role(role):
    def inner(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(inner)

admin_view = check_role('Admin')(admin_view)
librarian_view = check_role('Librarian')(librarian_view)
member_view = check_role('Member')(member_view)
