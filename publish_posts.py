import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangogirls.settings")

# Initialize Django
django.setup()

# Now you can import and use your models
from blog.models import Post

# Retrieve all Post objects
all_posts = Post.objects.all()

# Iterate through each Post object and call the publish() method
for post in all_posts:
    post.publish()
