from rest_framework import serializers

from post.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('__all__')