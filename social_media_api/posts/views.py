from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import CustomUser


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def followuser(request, user_id):
    users = CustomUser.objects.all()
    user_to_follow = get_object_or_404(users, id=user_id)

    if request.user == user_to_follow:
        return Response({"error": "You cannot follow yourself."}, status=400)

    request.user.following.add(user_to_follow)
    return Response({"message": "Followed successfully"})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollowuser(request, user_id):
    users = CustomUser.objects.all()
    user_to_unfollow = get_object_or_404(users, id=user_id)

    request.user.following.remove(user_to_unfollow)
    return Response({"message": "Unfollowed successfully"})

