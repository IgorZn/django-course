import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import My_Roles, Users

def del_table():
    d_users = Users.objects.filter().delete()
    d_roles = My_Roles.objects.filter().delete()

if __name__ == '__main__':
    del_table()