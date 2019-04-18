from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Django")


def detail(request, num, num1):
    return HttpResponse("detail-%d-%d" % (num, num1))  # "{0},{1}".format(num, num1)


from .models import Grades


def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/grades.html', {"grades": gradesList})


from .models import Students


def students(request):
    studentsList = Students.objects.all()
    return render(request, 'myApp/students.html', {"students": studentsList})


def grades_students(request, num):
    # 获取对应的班级对象
    grade = Grades.objects.get(pk=num)
    # 获取班级下所有学生对象列表
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentsList})
