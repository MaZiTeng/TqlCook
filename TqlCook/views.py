from django.shortcuts import render
from TqlCook.models import Recipe, Like


def home(request):
    # bing搜索没做，等着吧
    mostViewedRecipes = Recipe.objects.order_by('-views')[:6]
    context_dict = {}
    context_dict['recipes'] = mostViewedRecipes
    return render(request, 'home.html', context_dict)


def searchResult(request):
    return render(request, 'search.html')


def category(request):
    return render(request, 'category.html')


def recipe(request, recipe_id):
    selectedRecipe = Recipe.objects.get(id=recipe_id)
    mostViewedRecipes = Recipe.objects.order_by('?')[:3]
    likes = Like.objects.get(recipe_id_id=recipe_id).count()
    context_dict = {}
    # 菜谱
    context_dict['recipe'] = selectedRecipe
    # 推荐菜
    context_dict['recipes'] = mostViewedRecipes
    # 点赞
    context_dict['likes'] = likes

    return render(request, 'recipe.html', context_dict)


def auth(request):
    return render(request, 'auth.html')
