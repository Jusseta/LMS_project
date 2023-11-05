from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from education.models import Subscription
from education.serializers.subscription import SubscriptionSerializer


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Создание подписки"""
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Добавление владельца при создании подписки"""
        new_subscription = serializer.save()
        new_subscription.user = self.request.user
        new_subscription.save()


class SubscriptionListAPIView(generics.ListAPIView):
    """Список подписок"""
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """Удаление подписки"""
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
