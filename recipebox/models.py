from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite = models.ManyToManyField('RecipeModel', null=False, blank=True, related_name='favorite')

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    objects = models.aggregates_all
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    timereq = models.CharField(max_length=15)
    instructions = models.TextField()


def __str__(self):
    return self.title
