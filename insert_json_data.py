# run using python manage.py shell

import json
from posts.models import Post

with open('posts.json') as fp:
    posts_json = json.load(fp)

for post in posts_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()
