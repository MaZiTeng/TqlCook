from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class UserProfile(models.Model):
    id = models.IntegerField(default=0, auto_created=1, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=64)
    # password = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='profile_images', null=True)
    api = models.CharField(max_length=256, null=True)
    auth = models.IntegerField(default=1)  # 权限
    last_access_time = models.DateTimeField()


class Category(models.Model):
    id = models.IntegerField(default=1000, auto_created=1, primary_key=True)
    category = models.CharField(max_length=64)


class Recipe(models.Model):
    id = models.IntegerField(default=2000, auto_created=1, primary_key=True)
    name = models.CharField(max_length=128)
    time = models.DateField(null=True)
    ingredient = models.TextField()
    method = models.TextField()
    views = models.IntegerField(default=0)
    images = models.TextField()


class Comment(models.Model):
    id = models.IntegerField(default=3000, auto_created=1, primary_key=True)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField()


class RecipeCategory(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Like(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time = models.DateField()
