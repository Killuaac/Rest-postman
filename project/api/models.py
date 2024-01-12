from django.db import models
from rest_framework.authtoken.admin import User


class Posts(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
