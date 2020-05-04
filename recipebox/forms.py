from django import forms
from recipebox.models import Author

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    timereq = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'bio'
        ]