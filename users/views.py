# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from users.models import Payment
from users.serializers import PaymentSerializer, UserSerializer
# from users.services import create_stripe_price, create_stripe_session, create_stripe_product


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method',)
    ordering_fields = ('date',)


    # search_fields = ('payment_method',)
