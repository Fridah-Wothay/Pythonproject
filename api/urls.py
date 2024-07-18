from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import classesListView
from .views import ClassPeriodListView


urlpatterns = [
    path("student/", StudentListView.as_view(), name = "student_list_view"),
    path("teacher/", TeacherListView.as_view(), name = "teacher_list_view"),
    path("classes/",  classesListView.as_view(),name = "classes_list_view"),
    path("course/",  courseListView.as_view(),name = "course_list_view"),
    path("classperiod/",  ClassPeriodListView.as_view(),name = "classperiod_list_view"),
]