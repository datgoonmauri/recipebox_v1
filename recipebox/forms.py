from django import forms
from recipebox.models import Author


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    timereq = forms.CharField(max_length=15)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class AddAuthorForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Author
        fields = [
            'name',
            'bio'
        ]

class LoginUser(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)