from django.shortcuts import render
# 导入HttpResponse模块
from django.http import HttpResponse
from book.models import BookInfo


# Create your views here.

# 定义视图函数
def index(request):
    books=BookInfo.objects.all()
    print(books)

    return HttpResponse('index')

# 增加数据
# 导入BookInfo
# 方式一
from book.models import BookInfo
# book=BookInfo(
#     name='python入门',
#     pub_date='2010-6-3'
# )
# book.save()

# 方式二
# BookInfo.objects.create(
#     name='测试开发入门',
#     pub_date='2030-9-5',
#     readcount=100022
# )
# 修改数据
# 方式一
# book=BookInfo.objects.get(id=5)
# book.name='运维开发入门'
# book.save()


# 方式二
BookInfo.objects.filter(id=5).update(name='爬虫入门',commentcount=123)



# 删除数据
# 方式一
# book=BookInfo.objects.get(id=6)
# book.delete()

# 方式二
# BookInfo.objects.get(id=6).delete()
# BookInfo.objects.filter(id=5).delete()


# 查询
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常
try:
    book=BookInfo.objects.get(id=2)
except BookInfo.DoesNotExist:
    print('查询结果不存在')


# all查询多个结果
BookInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()



# 过滤查询
# 实现sql的where功能
# filter过滤多个结果
# exclude排除符合条件的显示剩下的结果
# get过滤单一结果


# 查询编号为1的图书
book=BookInfo.objects.get(id=1)

# 查询书名包含湖的书籍
BookInfo.objects.filter(name__contains='湖')

# 查询书名以部结尾
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的书籍
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3,5的书
BookInfo.objects.filter(id__in=[1,3,5])

# 查询编号大与3
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的
BookInfo.objects.filter(pub_date__gt='1990-1-1')


# 两个属性相比较
from django.db.models import F
# 语法：模型类名.objects.filter(属性名__运算符=F('第二个属性名'))

# 查询阅读量大于评论量的书
BookInfo.objects.filter(readcount__gt=F('commentcount'))

# 并且查询
# 查询阅读量大于20，并且编号小于3的书
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

# 或者查询

from django.db.models import Q
# 或者语法：模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)
# not 非 语法：在Q前面加～
# 查询阅读量大于20，或者编号小于3的图书
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))


# 查询编号不等于3
BookInfo.objects.filter(~Q(id=3))








































