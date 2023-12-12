#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2023 - 2023 Gosu, Inc. All Rights Reserved 
#
# @Time    : 2023/12/12 13:45
# @Author  : GosuXX
# @File    : views.py.py
import os

from django.shortcuts import render


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyDjango.settings")


def runoob(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'demo.html', context)


