from django.db import models
from course.models import Course 

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    personal_image = models.ImageField(upload_to='trainees/images/', null=True, blank=True)

    def __str__(self):
        return self.name