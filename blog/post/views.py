from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from api.authentication import TokenAuthentication
from .models import Post
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .serializers import PostSerializer
# from ..api.permissions import IsStaffEditorPermission

## To create generic API views
class PostListCreateAPIView(
    StaffEditorPermissionMixin,  # For users permissions
    UserQuerySetMixin,
    generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    """
    This StaffEditorPermissionMixin has been used in place of the comment permissions commands below
    ## Check the settings for authentication settings for users
    
    ## To add permission to API
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] #OR
    # permission_classes = [permissions.DjangoModelPermissions]
    """
    
    def perform_create(self, serializer):
        # serializer.save(username.request.user)
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        # or None
        if content is None:
            content=title
        serializer.save(user=self.request.user, content=content)
        # send a Django signal




class PostDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,  # For users permissions
    generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateAPIView(
    StaffEditorPermissionMixin,  # For users permissions
    generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


    def perform_update(self, serializer):
        
        instance = serializer.save()
        if not instance.content:
            instance.content=instance.title


class PostDestroyAPIView(
    StaffEditorPermissionMixin, # For users permissions
    generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


    def perform_destroy(self, instance):
       #instance
       super().perform_destroy(instance)



# # Mxins and a generic class view

class PosttMixin(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field ='pk'

    #To define the get method using the generic class view
    def get(self, request,*args, **kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs) ## This will return the the retrieve function if pk is present
        return self.list(request,*args, **kwargs)
    
    ##To define the post method using the generic class view
    def post(self, request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(username.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        # or None
        if content is None:
            content="This is me"
        serializer.save(content=content)
        # send a Django signal
