import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtube.settings")

import django
django.setup()

import random
from home.models import *
from faker import Faker
fake = Faker()

def populate():
    for i in range(100):
        obj = People.objects.create(name = fake.name(), email = fake.email(),
                                           about = fake.text(), age = random.randint(1,100))

        for i in range(0, random.randint(0,30)):
            c, _ = Colors.objects.get_or_create(color_code = fake.color())
            obj.colors.add(c)
            PeopleAddress.objects.create(people = obj, address = fake.address())

def main():
    populate()

if __name__ == "__main__":
    main()