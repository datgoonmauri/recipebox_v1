from django.shortcuts import render,reverse,HttpResponseRedirect
from recipebox.models import RecipeModel, Author
from recipebox.forms import AddRecipeForm, AddAuthorForm, LoginUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    data = RecipeModel.objects.all
    return render(request, "index.html", {'data': data})


def author(request, id=0):
    data = Author.objects.filter(id=id)[0]
    recipes = RecipeModel.objects.filter(author=id)
    return render(request, "author.html", {'data': data, 'recipes': recipes})


@staff_member_required
def add_author(request):
        html = 'generic_form.html'
        if request.method == "POST":
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(
                    username=data['username'],
                    password=data['password']
                )
                author = Author.objects.create(
                    name=data['name'],
                    bio=data['bio'],
                    user=user
                )
                return HttpResponseRedirect(reverse('homepage'))
        form = AddAuthorForm()
        return render(request,html,{'Form':form})


def recipe(request, id=1):
    data = RecipeModel.objects.filter(id=id)[0]
    return render(request, "recipe.html", {'data': data})

@login_required
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
    if not request.user.is_staff:
        form.fields['author'].queryset = Author.objects.filter(name=request.user.author.name)
    return render(request, html, {'Form':form})


def loginview(request):
    html = "generic_form.html"
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request,user)
                return HttpResponseRedirect(request.GET.get('next',reverse('homepage')))
    form = LoginUser()
    return render(request, html, {'Form': form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

