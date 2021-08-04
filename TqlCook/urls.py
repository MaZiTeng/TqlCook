#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/1 11:46 下午
# @Author : mzt
# @Site : 
# @File : urls.py
# @Software: PyCharm

from django.urls import path
from TqlCook import views



urlpatterns = [
    path('index/', views.home, name='home'),
    path('search/', views.searchResult, name='searchResult'),
    path('category/', views.category, name='category'),
    path('recipe/', views.recipe, name='recipe'),
    path('auth/', views.auth, name='auth'),
]
