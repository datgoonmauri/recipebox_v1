from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
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
	return render(request, html, {'Form': form})


def recipe(request, id):
	data = RecipeModel.objects.get(id=id)
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
	form = AddRecipeForm(request.POST)
	return render(request, html, {'Form': form})


def loginview(request):
	html = "generic_form.html"
	if request.method == "POST":
		form = LoginUser(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(request, username=data['username'], password=data['password'])
			if user:
				login(request, user)
				return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
	form = LoginUser()
	return render(request, html, {'form': form})


def logoutview(request):
	logout(request)
	return HttpResponseRedirect(reverse('homepage'))


@login_required
def edit_recipe(request, id):
	recipe = get_object_or_404(RecipeModel, pk=id)
	if request.user.author == recipe.author or request.user.is_superuser:
		if request.method == 'POST':
			form = AddRecipeForm(request.POST, instance=recipe)
			form.save()
			return HttpResponseRedirect(reverse('recipe', args=(id,)))

		form = AddRecipeForm(instance=recipe)
		return render(request, "generic_form.html", {'Form': form})


@login_required
def favorite(request, id):
	request.user.author.favorite.add(RecipeModel.objects.get(id))
	return HttpResponseRedirect(reverse('recipe', args=(id, )))


@login_required
def unfavorite(request, id):
	request.user.author.favorite.remove(RecipeModel.objects.get(id))
	return HttpResponseRedirect(reverse('recipe', args=(id,)))
