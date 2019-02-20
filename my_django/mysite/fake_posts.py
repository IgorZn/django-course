import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()

### FAKE POP SCRIPT
import random
from blog.models import Post
from faker import Faker

from django.contrib.auth.models import User
from django.utils import timezone

all_id = Post.objects.filter(status='published').values_list('id', flat=True)
tags = 'contemporary jazz Saint Louis neo soul Guayas jazz fusion gospel r&b/soul jazz 80s r&b chillwave new age Missouri vaporwave instrumental soul blues chillout funk'.split()



def add_tags_to_post(N=5):
    for entry in range(N):
        tag1 = random.choice(tags)
        tag2 = random.choice(tags)
        tag3 = random.choice(tags)
        addTag = Post.objects.get(id=all_id[entry])
        addTag.tags.add(tag1, tag2, tag3)



# user = User.objects.get(id=1)

# fakegen = Faker()
#
# def populate(N=5):
#     for entry in range(N):
#         f_title = fakegen.sentences(nb=1, ext_word_list=None)[0]
#         f_slug = f_title.replace(' ','-').replace('.','')
#         f_body = fakegen.paragraph(nb_sentences=10, variable_nb_sentences=True, ext_word_list=None)
#         post = Post.objects.get_or_create(title=f_title, slug=f_slug, author=user, body=f_body, status='published')




if __name__ == '__main__':
    add_tags_to_post(len(all_id))
    # print(all_id, tag)
    # print("Population script!")
    # populate(20)
    # print("Population complete!")