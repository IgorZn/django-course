import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from blog.models import Post

post = Post.objects.get(id=63)
post.tags.remove('django')
post.tags.add()
