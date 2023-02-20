from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    Question =models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text=models.CharField(max_length=200,default=0)
    gender=models.CharField(max_length=10,default=0)

class Student(models.Model):
    name = models.CharField(max_length=200)
    age=models.IntegerField(default=0)
