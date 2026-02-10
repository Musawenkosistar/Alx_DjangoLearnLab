# Permissions & Groups Setup

## Groups
- Admins: can_create, can_edit, can_delete, can_view
- Editors: can_create, can_edit, can_view
- Viewers: can_view

## Applying Permissions
- Views use @permission_required('relationship_app.<permission>', raise_exception=True)
- Users without permissions receive 403 errors
- Groups are automatically created after migrations via AppConfig signal

