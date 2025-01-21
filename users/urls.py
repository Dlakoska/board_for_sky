from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserCreateAPIView, ResetPasswordView, ResetPasswordConfirmView

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("reset_password/", ResetPasswordView.as_view(), name="reset_password"),
    path("reset_password_confirm/", ResetPasswordConfirmView.as_view(), name="reset_password_confirm"),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]
