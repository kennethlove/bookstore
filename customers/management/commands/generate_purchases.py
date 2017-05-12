from django.core.management.base import BaseCommand, CommandError

import factory

from ...factories import PurchaseFactory
from ...models import Purchase


class Command(BaseCommand):
    help = 'Generate N-number Purchases'

    def add_arguments(self, parser):
        parser.add_argument('num', nargs='?', default=10, type=int)

        parser.add_argument(
            '--clear',
            action='store_true',
            dest='clear',
            default=False,
            help='Clear out all Purchases before generating new'
        )

    def handle(self, *args, **options):
        if options['clear']:
            Purchase.objects.all().delete()

        factory.build_batch(PurchaseFactory, size=options['num'])
        self.stdout.write(
            self.style.SUCCESS('Successfully generated %s purchase(s)' % options['num'])
        )