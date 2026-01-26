"""
Django Management Command: Change Admin Username
Usage: python manage.py change_admin_username <old_username> <new_username>
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Change username for admin/superuser account'

    def add_arguments(self, parser):
        parser.add_argument('old_username', type=str, help='Current username')
        parser.add_argument('new_username', type=str, help='New username')

    def handle(self, *args, **options):
        old_username = options['old_username']
        new_username = options['new_username']

        try:
            # Check if old user exists
            try:
                user = User.objects.get(username=old_username)
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'❌ User "{old_username}" not found!')
                )
                return

            # Check if new username already exists
            if User.objects.filter(username=new_username).exists():
                self.stdout.write(
                    self.style.ERROR(
                        f'❌ Username "{new_username}" already exists! '
                        f'Please choose a different username.'
                    )
                )
                return

            # Change username
            old_username_backup = user.username
            user.username = new_username
            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Successfully changed username!\n'
                    f'   Old username: {old_username_backup}\n'
                    f'   New username: {new_username}\n'
                    f'📝 You can now login with the new username.'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error: {e}')
            )
