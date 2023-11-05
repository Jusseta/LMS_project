from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from users.models import User


@shared_task
def block_inactive_user():
    """Блокировка пользователей, заходивших более месяца назад"""
    users = User.objects.all()
    today_date = timezone.now()

    for user in users:
        if user.last_login <= today_date - timedelta(days=30):
            user.is_active = False
            user.save()
