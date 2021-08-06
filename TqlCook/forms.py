#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/2 4:15 下午
# @Author : mzt
# @Site : 
# @File : forms.py
# @Software: PyCharm

from django import forms
from django.contrib.auth.models import User
from TqlCook.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'last_login', 'is_staff')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
