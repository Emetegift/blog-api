# Generated by Django 4.2.3 on 2023-08-12 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_author_post_conclusion_post_introduction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
