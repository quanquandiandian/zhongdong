from django.db import models

# Create your models here.
# 准备书籍列表信息的模板类
class BookInfo(models.Model):
    # 创建字段，字段类型
    name = models.CharField(max_length=10,unique=True)
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)



    class Meta:
        db_table='bookinfo'#修改表的名字


    def __str__(self):

        return self.name

# 准备人物列表信息的模板类
class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )

    name = models.CharField(max_length=10)
    gender = models.BooleanField(choices=GENDER_CHOICE,default=1)
    description=models.CharField(max_length=10,null=True)
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table='peopleinfo'

    def __str__(self):
        return self.name

    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
