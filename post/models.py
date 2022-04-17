from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    """
    Database Table used to store All posts
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    delete_flag = models.BooleanField(default=False)
class Like(models.Model):
    """
    Database Table used to store All likes based on the user
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)


