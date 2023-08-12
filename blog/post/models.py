import random
from django.conf import settings
from django.db import models
from django.db.models import Q #This will help query the lookup with error

# Create your models here.

User = settings.AUTH_USER_MODEL #Auth user

## To tag things to the product class
# TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras']

class PostQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2=self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    introduction = models.TextField(max_length=200, blank=True, null=True )
    subheadings = models.TextField(max_length=200, blank=True, null=True )
    conclusion = models.TextField(max_length=200, blank=True, null=True )
    author = models.CharField(max_length=100, blank=True, null=False, default='Author')
    enable_comments = models.BooleanField(default=True)
   

    objects = PostManager()

    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"

    @property
    def endpoint(self):
        return f"/products/{self.pk}/"
        
    @property
    def url(self):
        return self.get_absolute_url()

    @property
    def body(self):
        return self.content # This will basically change the content to body in the serializer

    def is_public(self) -> bool:
        return self.public ## This will return true or false
    def __str__(self):
        return self.title
