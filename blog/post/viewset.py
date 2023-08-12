from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    get -->list-->queryset
    get --> retrieve -->product instance Detail view
    post -->create a new item or instance
    put --> update an instance
    patch --> partial update
    delete --> destroy an instance or item
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk" #default
