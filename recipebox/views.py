from django.shortcuts import render,reverse,HttpResponseRedirect
from recipebox.models import RecipeModel, Author
from recipebox.forms import AddRecipeForm, AddAuthorForm

# Create your views here.


def index(request):
    data = RecipeModel.objects.all
    return render(request, "index.html", {'data': data})


def author(request, id=0):
    data = Author.objects.filter(id=id)[0]
    recipes = RecipeModel.objects.filter(author=id)
    return render(request, "author.html", {'data': data, 'recipes': recipes})

def add_author(request):
    html = 'generic_form.html'
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = AddAuthorForm()
    return render(request,html,{'Form':form})


def recipe(request, id=1):
    data = RecipeModel.objects.filter(id=id)[0]
    return render(request, "recipe.html", {'data': data})

def add_recipe(request):
    html = 'generic_form.html'
    # breakpoint()
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeModel.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                timereq=data['timereq'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm()

    return render(request, html, {'Form':form})
