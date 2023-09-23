from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (EmailVerificationView, UserProfileView,
                    UserRegistrationView, login, logout)

urlpatterns = [
    path('login/', login, name='login'),
    path('regisrtashion/', UserRegistrationView.as_view(), name='regisrtashion'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logut/', logout, name='logout'),
    path('verify<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]
