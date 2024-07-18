from django.db import models

# Create your models here.
class Classes(models.Model):
      educational_resources = models.CharField(max_length = 20)
      tables = models.PositiveSmallIntegerField()
      chairs = models.CharField(max_length = 20)
      room_size = models.PositiveSmallIntegerField()
      assignment = models.CharField(max_length = 20)
      capacity = models.PositiveSmallIntegerField()
      class_laptop = models.PositiveSmallIntegerField()
      Student_representative = models.CharField(max_length = 20)
      class_lessons = models.PositiveSmallIntegerField()
      learning_hours = models.PositiveSmallIntegerField()



def __str__(self):
        return f"{self.educational_resources} {self.tables}"









