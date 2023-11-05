from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from education.models import Course, Subscription


@shared_task
def send_update_course_message(course_id):
    """Создание сообщения для отправки по почте при обновлении курса"""
    course = Course.objects.get(pk=course_id)
    subscription = Subscription.objects.filter(course=course_id)
    for sub in subscription:
        send_mail(
            subject="Обновление курса",
            message=f"Курс '{course.title}' обновлен. Заходите посмотреть новые уроки.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.user.email],
            fail_silently=True
        )
