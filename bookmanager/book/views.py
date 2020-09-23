from django.shortcuts import render
# 导入HttpResponse模块
from django.http import HttpResponse
from django.http import HttpRequest


# Create your views here.

# 定义视图函数
def index(request):
    context={
        'name':'詹姆斯'
    }
    return render(request,'index.html', context=context)