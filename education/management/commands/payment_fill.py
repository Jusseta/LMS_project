from django.core.management import BaseCommand
from education.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment1 = Payment.objects.create(
            payment_amount=5000,
            payment_method='cash'
        )
        payment1.save()

        payment2 = Payment.objects.create(
            payment_amount=8000,
            payment_method='transfer'
        )
        payment2.save()
