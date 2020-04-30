from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    timereq = models.CharField(max_length=15)
    instructions = models.TextField()

    def __str__(self):
        return self.title