from django.core.management.base import BaseCommand
from myapp2.models import Client
from random import choice as ch, randint as ri
from datetime import datetime


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        streets = ['green', 'purple', 'republic', 'garden', 'friendly', 'lenin st.']
        for i in range(1, 21):
            number = (f'+7({ri(0, 9)}{ri(0, 9)}{ri(0, 9)}){ri(0, 9)}{ri(0, 9)}'
                      f'{ri(0, 9)}-{ri(0, 9)}{ri(0, 9)}-{ri(0, 9)}{ri(0, 9)}')
            client = Client(name=f'client{i}', email=f'client{i}@example.com', telephone_number=number,
                            address=f'street {ch(streets)}, home {ri(1, 100)}', date_register=datetime.now())
            client.save()
            self.stdout.write(f'{client}')
