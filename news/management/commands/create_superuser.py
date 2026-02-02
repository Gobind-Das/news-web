"""
Django Management Command: Create Superuser
Usage: python manage.py create_superuser
Reads DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD from environment variables.
"""

import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser using environment variables DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not username:
            self.stdout.write(
                self.style.ERROR('❌ DJANGO_SUPERUSER_USERNAME environment variable not set!')
            )
            return

        if not password:
            self.stdout.write(
                self.style.ERROR('❌ DJANGO_SUPERUSER_PASSWORD environment variable not set!')
            )
            return

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Successfully updated password for existing superuser: {username}\n'
                    f'📝 You can now login with the new password from environment variables.'
                )
            )
            return

        try:
            user = User.objects.create_user(username=username, password=password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Successfully created superuser: {username}\n'
                    f'📝 You can now login with the credentials from environment variables.'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error creating superuser: {e}')
            )