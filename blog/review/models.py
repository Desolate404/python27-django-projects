from django.db import models
from post.models import Post, User

class Like(models.Model):
    user = models.ForeignKey(User, related_name='Likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='Likes', on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)