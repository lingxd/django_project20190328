from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Django")


def detail(request, num, num1):
    return HttpResponse("detail-%d-%d" % (num, num1))  # "{0},{1}".format(num, num1)


from .models import Students, Grades

from django.db.models import F, Q


def grades(request):
    # 去模板里取数据
    # gradesList = Grades.objects.all()
    gradesList = Grades.objects.filter(gboynum__gt=F('ggirlnum'))
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/grades.html', {"grades": gradesList})


def students(request):
    # studentsList = Students.objects.all()
    studentsList = Students.stuObj1.all()
    return render(request, 'myApp/students.html', {"students": studentsList})


def students_MultipleObjectsReturned(request):
    # 会出现异常 MultipleObjectsReturned
    studentsList = Students.stuObj1.get(sgender=True)
    return HttpResponse("===========")


# 显示前5条学生信息
def students_first5(request):
    studentsList = Students.stuObj1.all()[0:5]
    return render(request, 'myApp/students.html', {"students": studentsList})


# 分页显示学生信息
def students_page(request, page):
    # 0-5   5-10  10-15
    # 1      2      3
    # page*5    
    page = int(page)
    studentsList = Students.stuObj1.all()[(page - 1) * 5:page * 5]
    return render(request, 'myApp/students.html', {"students": studentsList})


from django.db.models import Max


def students_query(request):
    # studentsList = Students.stuObj1.all()
    # studentsList = Students.stuObj1.filter(sname__contains="羊")
    # studentsList = Students.stuObj1.filter(sname__endswith="狼")
    # studentsList = Students.stuObj1.filter(pk__in=[2, 4, 6, 8, 10])
    # studentsList = Students.stuObj1.filter(sage__gt=20)
    # studentsList = Students.stuObj1.filter(lastTime__year=2019)
    # studentsList = Students.stuObj1.filter(sname__contains="%")
    # 描述中带有喜羊羊这三个字的数据是属于哪个班级的
    grade = Grades.objects.filter(students__scontend__contains="喜羊羊")
    print(grade)
    # studentsList = Students.stuObj1.filter(Q(pk__lte=3) | Q(sage__gt=29))
    studentsList = Students.stuObj1.filter(~Q(pk__lte=3))
    maxAge = Students.stuObj1.aggregate(Max("sage"))
    print(maxAge)
    return render(request, 'myApp/students.html', {"students": studentsList})


def addstudents(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.create_student("潇洒哥", 20, True, "我叫潇洒哥", grade, "2019-4-9", "2019-4-9")
    stu.save()
    return HttpResponse("增加成功")


def addstudents2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj1.create_student("武太郎", 55, True, "我是灰太狼的太太太太爷爷", grade, "2019-4-9", "2019-4-9")
    stu.save()
    return HttpResponse("增加成功")


def grades_students(request, num):
    # 获取对应的班级对象
    grade = Grades.objects.get(pk=num)
    # 获取班级下所有学生对象列表
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentsList})
