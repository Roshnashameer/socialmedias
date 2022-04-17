from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from post.models import Post
from post.serilizers import PostSerializer, PostLikeSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class PostListing(generics.ListAPIView):
    """Api for client code suggestion"""
    permissions_classes = ['AllowAny']
    serializer_class = PostSerializer
    queryset = Post.objects.filter(delete_flag=False)

class PostCreateView(generics.CreateAPIView):
    """Api for client code suggestion"""
    permissions_classes = ['AllowAny']
    serializer_class = PostSerializer


class PostDeleteView(generics.UpdateAPIView):
    """Api for client code suggestion"""
    permissions_classes = ['AllowAny']
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostUpdateView(generics.UpdateAPIView):
    """Api for client code suggestion"""
    permissions_classes = ['AllowAny']
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class LikeView(generics.CreateAPIView):
    """Api for client code suggestion"""
    permissions_classes = ['AllowAny']
    serializer_class = PostLikeSerializer




