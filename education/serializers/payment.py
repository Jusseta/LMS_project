from rest_framework import serializers
from education.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор модели платежа"""
    class Meta:
        model = Payment
        fields = '__all__'
