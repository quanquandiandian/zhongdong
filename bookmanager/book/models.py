from django.db import models

# Create your models here.
# 准备书籍列表信息的模板类
class BookInfo(models.Model):
    # 创建字段，字段类型
    name = models.CharField(max_length=10)

# 准备人物列表信息的模板类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()

    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
