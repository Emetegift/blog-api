## General serializer that is link to the post serializer
from rest_framework import serializers

#For  a user to get his or her  other products
class UserPostInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(  #This will handle the detail view (retrieve)
        view_name='post-detail',
        lookup_field = 'pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True) ## This will display the actual user's name
    id = serializers.IntegerField(read_only=True)
    # email =serializers.EmailField(read_only=True)

    