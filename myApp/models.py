from django.db import models


# Create your models here.


class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gname

    class Meta:
        db_table = "grades"
        ordering = []


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)

    def create_student(self, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = self.model()
        # print(type(stu))
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime = lastT
        stu.createTime = createT
        return stu


class Students(models.Model):
    # 定义一个类方法创建对象
    @classmethod
    def create_student(cls, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = cls(sname=name, sage=age, sgender=gender, scontend=contend, sgrade=grade, lastTime=lastT,
                  createTime=createT,
                  isDelete=isD)
        return stu

    # 自定义模型管理器
    # 当自定义模型管理器，objects就不存在了
    stuObj = models.Manager()
    stuObj1 = StudentsManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sname

    class Meta:
        db_table = "students"
        ordering = ['id']
