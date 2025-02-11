
from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from  course.models import Course
from  classes.models import Classes
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from .serializers import StudentSerializer
from .serializers import ClassesSerializer
from .serializers import CourseSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from rest_framework.response import Response
class StudentListView(APIView):
    def get (self,request):
        student = Student.objects.all()
        serializer =StudentSerializer(Student,many=True)
        return Response(serializer.data)
class  CourseListView(APIView):
    def get(self,request):
        courses= Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get (self,request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers,many=True)
        return Response(serializer.data)
class  ClassesListView (APIView):
    def get (self,request):
        classes = Classes.objects.all()
        serializer =   ClassesSerializer(classes,many=True)
        return Response(serializer.data)
class ClassPeriodListView(APIView):
    def get (self,request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod,many=True)
        return Response(serializer.data)