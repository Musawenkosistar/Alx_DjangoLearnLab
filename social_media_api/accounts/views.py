from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import CustomUser

from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "bio": user.bio,
            "followers_count": user.followers.count(),
            "following_count": user.following.count(),
        })


# -------------------------
# FOLLOW / UNFOLLOW SYSTEM
# -------------------------

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

