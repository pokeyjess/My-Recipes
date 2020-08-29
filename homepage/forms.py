from django import forms
from homepage.models import Recipe, Category
'''
class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    summary = forms.CharField(max_length=100)
    instructions = forms.CharField(widget=forms.Textarea)
'''
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "category", "summary", "instructions"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]

    # category = forms.CharField(max_length=80)
    # description = forms.CharField(max_length=200)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)