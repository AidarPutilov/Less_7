from datetime import datetime
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import (
    create_stripe_price,
    create_stripe_product,
    create_stripe_sessions,
)


class PaymentsListAPIView(generics.ListAPIView):
    """API GET для платежей."""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = (
        "course",
        "lesson",
        "method",
    )
    ordering_fields = ("date",)
    search_fields = ("method",)


class PaymentCreateAPIView(generics.CreateAPIView):
    """API CREATE для платежа."""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product_id = create_stripe_product(payment)
        price_id = create_stripe_price(payment.cost, product_id)
        session_id, payment_link = create_stripe_sessions(price_id)
        payment.session_id = session_id
        payment.link = payment_link
        payment.date = datetime.now().date()
        payment.save()


class UserCreateAPIView(generics.CreateAPIView):
    """API CREATE для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """API GET для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """API RETRIVE для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """API PATCH для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    """API DELETE для пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
