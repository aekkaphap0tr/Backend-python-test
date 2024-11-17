from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)  
    initials = models.CharField(max_length=10)  
    address = models.TextField() 


class Classroom(models.Model):
    grade_level = models.CharField(max_length=10)
    group = models.IntegerField() 
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')



class Teacher(models.Model):
    gender = [('M', 'Male'), ('F', 'Female')] 
    name = models.CharField(max_length=100) 
    surname = models.CharField(max_length=100) 
    sex = models.CharField(max_length=1, choices=gender)  
    classrooms = models.ManyToManyField(Classroom, related_name='teachers') 


class Student(models.Model):
    gender = [('M', 'Male'), ('F', 'Female')] 
    name = models.CharField(max_length=100) 
    surname = models.CharField(max_length=100) 
    sex = models.CharField(max_length=1, choices=gender) 
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students') 

