from django.core.management.base import BaseCommand
from covid.models import Covid
import csv



class Command(BaseCommand):
    help = 'Populates database from the information in the specified csv file'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str,
                            help='Indicates the path to .csv file')

    def handle(self, *args, **kwargs):
        csvfile = kwargs['csvfile']

        with open(csvfile) as file:
            data = csv.DictReader(file)

            for item in data:

                Covid.objects.get_or_create(name=item['name'])[0]