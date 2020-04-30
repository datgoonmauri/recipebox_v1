from django.shortcuts import render
from recipebox.models import RecipeModel, Author
# Create your views here.


def index(request):
    data = RecipeModel.objects.all
    return render(request, "index.html", {'data': data})


def author(request, id=0):
    data = Author.objects.filter(id=id)[0]
    recipes = RecipeModel.objects.filter(author=id)
    return render(request, "author.html", {'data': data, 'recipes': recipes})


def recipe(request, id=1):
    data = RecipeModel.objects.filter(id=id)[0]
    return render(request, "recipe.html", {'data': data})
