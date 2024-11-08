from django.core.management.base import BaseCommand
from seed import FakeData

# fake_data = FakeData()
# print("i am running the funtion 1")
# fake_data.add_colors()
# print("i am running the functi 2.")
# fake_data.add_peoples()

class Command(BaseCommand):
    help = 'Seeds the database with fake data'
    def handle(self, *args, **options):
        fake_data = FakeData()
        fake_data.add_colors()
        fake_data.add_peoples()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with fake data.'))