from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups_permissions(sender, **kwargs):
    # Only run for your app
    if sender.name == 'relationship_app':
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Example: assign permissions
        can_add_book = Permission.objects.get(codename='can_add_book')
        can_change_book = Permission.objects.get(codename='can_change_book')
        can_delete_book = Permission.objects.get(codename='can_delete_book')

        editors.permissions.set([can_add_book, can_change_book])
        viewers.permissions.set([])
        admins.permissions.set([can_add_book, can_change_book, can_delete_book])
