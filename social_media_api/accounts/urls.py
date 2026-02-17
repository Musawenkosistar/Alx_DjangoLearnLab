from django.urls import path
<<<<<<< HEAD
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
=======
from .views import RegisterUserView, CustomObtainAuthToken, ProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
>>>>>>> afb93ecba8bc6ee8f5e3490d59b66bcbe1f64375
]
