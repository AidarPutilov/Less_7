# from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import PaymentViewSet

from users.apps import UsersConfig


# , PaymentCreateAPIView
# , UserCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
] + router.urls
