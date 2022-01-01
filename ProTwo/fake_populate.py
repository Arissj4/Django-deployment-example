import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def make_populte (N=5):

    for a in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        User.objects.get_or_create(First_name=fake_first_name, Last_name=fake_last_name, Email=fake_email)

if __name__ == "__main__":
    print("Making Rocords!")
    make_populte(20)
    print("Done!")