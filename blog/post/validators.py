## for custom validation

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Post


## This validation function below can be used when you want a particular type of input from users, e.g using no_hello
def validate_title_no_hello(value):
      if "hello"in value.lower():
            raise serializers.ValidationError(f" {value}: Hello is not allowed")
      return value


unique_product_title = UniqueValidator(queryset=Post.objects.all(), lookup='iexact')


