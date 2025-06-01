from django.db import models
from myapp.models import*

# Create your models here.
class student_from(models.Model):
    name=models.CharField(max_length=100)
    department_name=models.CharField(max_length=100)
    city_name=models.CharField(max_length=100)
    age=models.IntegerField()


class tacher_model(models.Model):
    id_number=models.IntegerField()
    tacher_name=models.CharField(max_length=100)
    city_name=models.CharField(max_length=100)
    age=models.IntegerField()





class course_model(models.Model):
    CSE =models.CharField(max_length=100)
    BBA=models.IntegerField()
    MATH=models.TextField()
    english=models.IntegerField()