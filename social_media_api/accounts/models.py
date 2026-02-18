from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404

User = get_user_model()


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def followuser(request, user_id):
    users = User.objects.all()
    user_to_follow = get_object_or_404(users, id=user_id)

    if request.user == user_to_follow:
        return Response({"error": "You cannot follow yourself."}, status=400)

    request.user.following.add(user_to_follow)
    return Response({"message": "Followed successfully"})

