"""
Django Management Command: Reset Admin Password
Usage: python manage.py reset_admin_password <username> <new_password>
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Reset password for admin/superuser account'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the admin account')
        parser.add_argument('new_password', type=str, help='New password for the admin account')

    def handle(self, *args, **options):
        username = options['username']
        new_password = options['new_password']

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Successfully reset password for user: {username}\n'
                    f'📝 You can now login with the new password.'
                )
            )
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'❌ User "{username}" not found!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error: {e}')
            )
