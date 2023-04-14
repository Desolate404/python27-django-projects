from django.db import models
from post.models import Post, User

class Like(models.Model):
    user = models.ForeignKey(User, related_name='Likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='Likes', on_delete=models.CASCADE)
