from django.core.management.base import BaseCommand

from key_server.key_management_system.tasks import delete_expired_keys


class Command(BaseCommand):
    help = "Deletes the keys in the database that have reached the expiration date."

    def handle(self, *args, **options):
        delete_expired_keys()
        self.stdout.write("Key Deletion finished", ending="")
