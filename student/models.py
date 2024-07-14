from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    country = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    student_class  = models.CharField(max_length = 20)
    locker_number = models.PositiveSmallIntegerField()
    student_mentor = models.CharField(max_length = 20)
    student_gurdian = models.CharField(max_length = 20)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"

