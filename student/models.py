from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=120)
    grade = models.PositiveIntegerField()
    major = models.CharField(max_length=120)

    def __str__(self):
        return self.name
