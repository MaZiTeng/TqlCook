#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/1 11:46 下午
# @Author : mzt
# @Site :
# @File : urls.py
# @Software: PyCharm

from django.urls import path
from TqlCook import views

app_name = 'TqlCook'

urlpatterns = [
    path('index/', views.home, name='home'),
    path('search/', views.searchResult, name='searchResult'),
    path('category/', views.category, name='category'),
    path('recipe/<int:recipe_id>', views.recipe, name='recipe'),
    path('auth/', views.auth, name='auth'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
