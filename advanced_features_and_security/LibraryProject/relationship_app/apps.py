from django.apps import AppConfig
from django.db.models.signals import post_migrate

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        post_migrate.connect(create_groups_and_permissions, sender=self)

def create_groups_and_permissions(sender, **kwargs):
    # Groups to create
    group_permissions = {
        "Admins": ["can_create", "can_edit", "can_delete", "can_view"],
        "Editors": ["can_create", "can_edit", "can_view"],
        "Viewers": ["can_view"],
    }

    for group_name, perms in group_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_codename in perms:
            try:
                perm = Permission.objects.get(codename=perm_codename)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                print(f"Permission {perm_codename} not found.")

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        # Place imports that need fully loaded apps here
        import relationship_app.signals  # if you have signal handlers
