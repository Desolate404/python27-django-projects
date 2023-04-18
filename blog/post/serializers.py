from rest_framework.serializers import ModelSerializer
from .models import Post
from review.serializers import CommentSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.Likes.all().count()
        comments = instance.comments.all()# все коменты
        rep['comments'] = CommentSerializer(comments, many=True).data
        return rep



