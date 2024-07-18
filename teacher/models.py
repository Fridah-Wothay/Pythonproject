from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 20)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    course = models.CharField(max_length = 20)
    teacher_resume = models.CharField(max_length = 20)
    national_id = models.PositiveSmallIntegerField()
    account_number = models.DateField()
    teaching_hours = models.PositiveSmallIntegerField()

    def __str__(self):
        return "f{self.first_name} {self.last_name}" 