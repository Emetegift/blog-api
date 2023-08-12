from django.shortcuts import render

# Create the API endpoint view
import json
from rest_framework.response import Response
# from django.forms.models import model_to_dict
# from products.models import Product
from rest_framework.decorators import api_view
# from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
     This is a Django Rest API view
     """
    pass
    # serializer = ProductSerializer(data=request.data)
    # if serializer.is_valid():
    #     # instance = serializer.save()
    #     print(serializer.data)
    #     return Response(serializer.data)
    



