from celery import shared_task
import requests
from django.utils import timezone
from time import time


from .models import Server


def ping_server(server):
    start = time()
    try:
        response = requests.get(f'https://{server.host_name}', params={'s': 'this?'})
        server.last_ping = timezone.now()
        server.last_ping_latency = 1000 * (time() - start)
    except requests.exceptions.RequestException as e:
        server.status = 'o'
    server.save()

@shared_task()
def ping_servers():
    for server in Server.objects.filter(
        status__in=('a', 'n', )
    ):
        ping_server(server)
