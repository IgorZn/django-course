import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

### FAKE POP SCRIPT
import random
from first_app.models import My_Roles, Users
from faker import Faker

fakegen = Faker()
roles_list = ['Guest', 'Girl', 'Firend', 'Huilo', 'Mudilo']

def add_role():
    r = My_Roles.objects.get_or_create(user_role=random.choice(roles_list))[0]
    print(r)
    r.save()
    return r

# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        role = add_role()
        print(role)

        # create the fake data for that entry
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.free_email()

        # create the user entry
        # User = Users.objects.get_or_create(role=role, first_name=fake_fname, last_name=fake_lname)
        User = Users.objects.get_or_create(role=role, first_name=fake_fname, last_name=fake_lname, email=fake_email)


if __name__ == '__main__':
    print("Population script!")
    populate(20)
    print("Population complete!")