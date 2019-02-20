import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()
from django.core.mail import send_mail
send_mail('Django mail', 'This e-mail was sent with Django.', 'igor.znamensky@gmail.com', ['igor.znamensky@gmail.com'], fail_silently=False,)