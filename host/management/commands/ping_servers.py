from django.core.management.base import BaseCommand, CommandError

from host.tasks import ping_servers


class Command(BaseCommand):
    help = 'Pings active servers.'

    def handle(self, *args, **options):

        verbosity = int(options['verbosity'])

        if verbosity:
            print('Pinging active servers...')

            ping_servers()
