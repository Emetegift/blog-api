from django import forms

from .models import Post

class ProductForms(forms.Model):
    class Meta:
        model =Post
        fields = [
            "title",
            'content'
        ]