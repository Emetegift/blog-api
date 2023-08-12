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
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # introduction = models.TextField()
    # subheadings = models.TextField()
    # conclusion = models.TextField()
    # author = models.CharField(max_length=100)
    # tags = models.CharField(max_length=200)
    # call_to_action = models.CharField(max_length=200)
    # featured_image = models.ImageField(upload_to='images/')
    # language = models.CharField(max_length=20)
    # estimated_read_time = models.CharField(max_length=20)
    enable_comments = models.BooleanField(default=True)
    # enable_social_sharing = models.BooleanField(default=True)




    objects = PostManager()

    # def get_absolute_url(self):
    #     return f"/api/products/{self.pk}/"

    # @property
    # def endpoint(self):
    #     return f"/products/{self.pk}/"
        
    @property
    def url(self):
        return self.get_absolute_url()

    @property
    def body(self):
        return self.content # This will basically change the content to body in the serializer

    def is_public(self) -> bool:
        return self.public ## This will return true or false
    
    # def get_tags_list(self):
    #     return [random.choice(TAGS_MODEL_VALUES)]

    def __str__(self):
        return self.title

    # @property
    # def sale_price(self):
    #     return "%.2f" %(float(self.price) * 0.8) 
    # """ 
    # This is used when a seller wants to give percentage discount of te main price 
    # by calculating the percentage that is to be given as discount
    # """
    # def get_discount(self):
    #     return "122"
