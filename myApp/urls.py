from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path('(\d+)/(\d+)/', views.detail),
    path('grades/', views.grades),
    path('students/', views.students),
    path('addstudents/', views.addstudents),
    path('students_MultipleObjectsReturned/', views.students_MultipleObjectsReturned),
    path('students_first5/', views.students_first5),
    path('addstudents2/', views.addstudents2),
    path('students_query/', views.students_query),
    re_path('students_page/(\d+)/', views.students_page),
    re_path('grades/(\d+)/', views.grades_students)
]
