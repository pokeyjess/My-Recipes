from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from homepage.models import Category, Recipe
from homepage.forms import RecipeForm, CategoryForm, LoginForm, SignUpForm

def index(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories })

# @login_required
def category(request, category_id):
    category_info = Category.objects.filter(id=category_id).first()
    recipe_list = Recipe.objects.filter(category=category_info)
    return render(request, "category.html", {"category": category_info, "recipes": recipe_list})

# @login_required
def recipe(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe.html", {"recipe": my_recipe})

@login_required
def recipe_form_view(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                Recipe.objects.create(title=data.get('title'), category=data.get('category'), summary=data.get('summary'), instructions=data.get('instructions'), recipe_image=data.get('recipe_image'))
                return HttpResponseRedirect(reverse("homepage"))
        form = RecipeForm()
        return render(request, "recipe_form.html", {"form": form})
    else:
        return HttpResponseForbidden("You must have admin privileges to access this page")

@login_required
def category_form_view(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form.save()
                return HttpResponseRedirect(reverse("homepage"))
        form = CategoryForm()
        return render(request, "category_form.html", {"form": form})
    else:
        return HttpResponseForbidden("You must have admin privileges to access this page")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
        return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

@login_required
def signup_view(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
                return HttpResponseRedirect(reverse("homepage"))
        form = SignUpForm()
        return render(request, "generic_form.html", {"form": form})
    else:
        return HttpResponseForbidden("You must have admin privileges to access this page")

@login_required
def recipe_edit(request, id):
    if request.user.is_staff:
        edit = get_object_or_404(Recipe, id=id)
        if request.method == "POST":
            form = RecipeForm(request.POST, request.FILES, instance=edit)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.save()
                return redirect('recipe', edit.pk)
        else:
            form = RecipeForm(instance=edit)
        return render(request, 'edit_recipe.html', {'form': form})
    else:
        return HttpResponseForbidden("You must have admin privileges to access this page")

@login_required
def category_edit(request, id):
    if request.user.is_staff:
        edit = get_object_or_404(Category, id=id)
        if request.method == "POST":
            form = CategoryForm(request.POST, request.FILES, instance=edit)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.save()
                return redirect('category', edit.pk)
        else:
            form = CategoryForm(instance=edit)
        return render(request, 'category_form.html', {'form': form})
    else:
        return HttpResponseForbidden("You must have admin privileges to access this page")
   
@login_required
def remove_recipe(request, id):
    if request.user.is_staff:
        recipe = get_object_or_404(Recipe, id=id)
        recipe.delete()
        return redirect('homepage')
    else:
        return HttpResponseForbidden("You must have admin privileges to access this page")

@login_required
def remove_category(request, id):
    if request.user.is_staff:
        category = get_object_or_404(Category, id=id)
        category.delete()
        return redirect('homepage')
    else:
        return HttpResponseForbidden("You must have admin privileges to access this page")
