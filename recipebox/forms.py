from django import forms
from django.forms import modelform_factory

from recipebox.models import Author, RecipeModel


class AddAuthorForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = [
            'name',
            'bio'
        ]


AddRecipeForm = modelform_factory(RecipeModel, exclude=[])


class LoginUser(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

