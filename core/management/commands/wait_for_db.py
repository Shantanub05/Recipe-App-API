from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for databases...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])  # type: ignore
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting for 1 sec...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available'))
