import os

from .models import User
from django.http import HttpResponse

from MyDjango.utils.log import Logger

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyDjango.settings")


def addUser(request):
    test1 = User(name='runoob', sex="male", age=18)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def query_all_user(request):
    list1 = f"{list(User.objects.all())}"
    return HttpResponse(f"<p> 查询到所有user: {list1} </p>")
