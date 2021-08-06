from django.shortcuts import render
from TqlCook.models import Recipe, Like, UserProfile, Comment, User, RecipeCategory
from django.contrib.auth.decorators import login_required
from TqlCook.forms import UserForm, UserProfileForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from datetime import datetime


def index(request):
    # bing搜索没做，等着吧
    mostViewedRecipes = Recipe.objects.order_by('-views')[:6]
    context_dict = {}
    context_dict['recipes'] = mostViewedRecipes
    return render(request, 'TqlCook/index.html', context_dict)


def searchResult(request):
    return render(request, 'TqlCook/search.html')


def category(request, category_id):
    recipeList = RecipeCategory.objects.filter(category_id_id=category_id)
    recipes = []
    for recipe in recipeList:
        recipes.append(Recipe.objects.get(pk=recipe.recipe_id_id))
    context_dict = {}
    context_dict['recipes'] = recipes
    return render(request, 'TqlCook/category.html', context_dict)


def recipe(request, recipe_id):
    request.session['recipe_id'] = recipe_id
    selectedRecipe = Recipe.objects.get(pk=recipe_id)
    mostViewedRecipes = Recipe.objects.order_by('?')[:3]
    likes = Like.objects.filter(recipe_id_id=recipe_id).count()

    # 判断当前用户是否点赞
    is_like = False
    user_id = int(get_server_side_cookie(request, 'user_id', '-1'))
    if Like.objects.filter(recipe_id_id=selectedRecipe.id, user_id_id=user_id).exists():
        is_like = True

    commentsTem = Comment.objects.filter(recipe_id_id=selectedRecipe.id)
    comments = []
    for i in commentsTem:
        print(i.user_id_id)
        print(UserProfile.objects.get(pk=0))

        comments.append([i.content, User.objects.get(pk=0)])

    context_dict = {}
    # 菜谱
    context_dict['recipe'] = selectedRecipe
    # 推荐菜
    context_dict['recipes'] = mostViewedRecipes
    # 点赞
    context_dict['likes'] = likes
    # 本人点赞
    context_dict['is_like'] = is_like
    # 评论
    context_dict['comments'] = comments

    #   数据库中view+1
    selectedRecipe.views += 1
    return render(request, 'TqlCook/recipe.html', context_dict)


# def auth(request):
#     return render(request, 'TqlCook/auth.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'TqlCook/index.html', context={  # 链接到主页
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = UserProfile.user.id
                return redirect(reverse('TqlCook/index.html'))  # 链接到主页
            else:
                print("非活跃用户")
                return render(request, 'TqlCook/login.html')  # 链接登录页面
        else:
            print(f"Invalid login details: {username}, {password}")
            return render(request, 'TqlCook/login.html')  # 链接登录页面
    else:
        return render(request, 'TqlCook/login.html')  # 链接登录页面


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('TqlCook/index.html'))


# 从服务器获取数据
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


@login_required
def add_comment(request):
    user_id = int(get_server_side_cookie(request, 'user_id', '-1'))
    recipe_id = int(get_server_side_cookie(request, 'recipe_id', '-1'))
    # form = CommentForm(instance=user_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.recipe_id_id = recipe_id
            form.user_id_id = user_id
            form.save(commit=True)
            return redirect(request.get_full_path())
        else:
            print(form.errors)
    return redirect(request.get_full_path())
