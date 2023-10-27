from rest_framework import serializers
from education.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор модели подписки"""

    class Meta:
        model = Subscription
        fields = '__all__'
