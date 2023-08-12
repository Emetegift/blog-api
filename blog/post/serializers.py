from rest_framework import serializers
from api.serializers import UserPublicSerializer ## This is regarded as the general serializer linked to the one above
from .models import Post
from rest_framework.reverse import reverse
# from .validators import validate_title
from . import validators


## Related fields and foreign key serializer. this will basicall list all the users posts links and title
class PostInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='post-detail',
        lookup_field = 'pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class PostSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True) #This will call all the values in the general serializers
    edit_url =  serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='post-detail',
        lookup_field = 'pk'
    )
    # email = serializers.EmailField(write_only=True) # Please note that this can be anything besides email
    # title = serializers.CharField(validators=[validate_title])
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # email = serializers.CharField(source='user.email', read_only=True)
    body = serializers.CharField(source='content') ## This will enable the content field that has been changed to body to reflect
    class Meta:
        model = Post
        fields =[
            'owner',
            'url',
            'edit_url',
            # 'email',
            'pk',
            'title',
            # 'my_discount',
            # 'related_product',
            # # 'my_user_data',
            # 'public',
            # 'endpoint',
        ]

    def  get_my_user_data(self, obj):
        return {
            "username": obj.user.username ## This will basically get the actual username
        }

    def get_edit_url(self, obj):
         # return f"/api/v2/products/{obj.pk}"  # OR
        request = self.context.get('request') # This is a get request because it is how serializers work 
        if request is None:
            return None
        return reverse("post-edit", kwargs={"pk":obj.pk}, request=request) # This will handle the update endpoint
       
