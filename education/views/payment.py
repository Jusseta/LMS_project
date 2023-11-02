from django.conf import settings
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
import stripe
from education.models import Payment
from education.serializers.payment import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """Вьюсет для платежей"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('pay_date',)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        payment.save()

        new_pay = serializer.save()
        stripe.api_key = settings.STRIPE_KEY

        new_pay = stripe.PaymentIntent.create(
            amount=serializer.data['payment_amount'],
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )

        new_pay.save()

    def retrieve_payment(self, payment_id):
        stripe.api_key = settings.STRIPE_KEY
        payment_intent = stripe.PaymentIntent.retrieve(payment_id.id,)
        return payment_intent
