from django.db import models

# Create your models here.

class Course(models.Model):
     course_name = models.CharField(max_length = 20)
     course_trainer = models.CharField(max_length = 20)
     course_description = models.CharField(max_length = 20)
     course_score = models.PositiveSmallIntegerField()
     coure_interest = models.CharField(max_length = 20)
     course_requirement = models.CharField(max_length = 20)
     course_id = models.PositiveSmallIntegerField()
     professor_attributes = models.CharField(max_length = 20)
     course_duration = models.PositiveSmallIntegerField()
     year_introduced = models.PositiveSmallIntegerField()

def _str_(self):
        return f"{self.first_name} {self.last_name}"
