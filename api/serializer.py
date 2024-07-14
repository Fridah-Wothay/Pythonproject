from django.shortcuts import render



from rest_framework import serializers
from student.models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

# class StudentSerializer(serializer.modellserializer):
#     class meta:
#         model = Student
#         fields = "--all--"


# class StudentListView(APIview):
#     def get(self,request):
#         students = Student.objects.all()   
#         serializer = StudentSerializer(student,many=True)  
#         return Response(serializer.data)   


