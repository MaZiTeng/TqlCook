from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def searchResult(request):
    return render(request, 'search.html')


def category(request):
    return render(request, 'category.html')


def recipe(request):
    return render(request, 'recipe.html')


def auth(request):
    return render(request, 'auth.html')
