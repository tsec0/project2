from .receivers import *

from django.urls import path, include

from accounts.views import SignUpView, SignOutView, SignInView, UserProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', UserProfileView.as_view(), name='current'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='user profile'),
    path('signin/', SignInView.as_view(), name='signin user'),
    path('signup/', SignUpView.as_view(), name='signup user'),
    path('signout/', SignOutView.as_view(), name='signout user'),
]
