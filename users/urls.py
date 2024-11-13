from django.urls import path
from rest_framework.routers import SimpleRouter
from users.views import (
    PaymentViewSet,
    UserCreateAPIView,
    UserDeleteAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig


app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    # Маршруты для модели User
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("view/", UserListAPIView.as_view(), name="list_view"),
    path("view/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_change"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="user_delete"),
    # Маршруты для работы с JWT-токенами
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
