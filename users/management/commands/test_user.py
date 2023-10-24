from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='vikashpur0@yandex.ru',
            first_name='User',
            last_name='Userov',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )
        user.set_password('1234qwer')
        user.save()
