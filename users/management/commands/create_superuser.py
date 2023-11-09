from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        superuser = User.objects.create(
            email='jstoronsky@testt.com',
            first_name='Admin',
            is_superuser=True,
            is_staff=True,
            role='admin'
        )

        superuser.set_password('Demon6600')
        superuser.save()
