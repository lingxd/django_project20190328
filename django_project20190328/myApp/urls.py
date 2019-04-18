from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path('(\d+)/(\d+)/', views.detail),
    path('grades/', views.grades),
    path('students/', views.students),
    re_path('grades/(\d+)/', views.grades_students)
]
