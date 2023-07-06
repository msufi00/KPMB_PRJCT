from django.db import models

# Create your models here.
class Course(models.Model):
    coursecode = models.CharField(max_length=4,primary_key=True)
    coursename = models.TextField(max_length=128)
    coursedate = models.DateField(blank=True, null=True)


class Student(models.Model):
    studentid = models.CharField(max_length=4,primary_key=True)
    studentname = models.TextField(max_length= 128)
    studentphone = models.CharField(max_length=20)
    mentorname = models.TextField(max_length=128)
    coursecode = models.ForeignKey(Course,on_delete=models.CASCADE )
# default sebelum ni sebaagai DCS , so kena buang kan default='UNKNOWN'