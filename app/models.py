from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    date_Created = models.DateTimeField(auto_now_add=True, null=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    modules = models.IntegerField(null=True, blank=True, default=0)
    materials = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

#rename later
class Taken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.user.username)+" -- "+str(self.course.name)


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    questions = models.IntegerField(null=True, blank=True, default=0)
    materials = models.URLField(null=True, blank=True)
    #time = models.DurationField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Result(models.Model):
    module = models.ForeignKey(Module, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, null=True)
    marks = models.IntegerField()

    def __str__(self):
        return str(self.user.username)+" -- "+str(self.module.name)


class Question(models.Model):
    module = models.ForeignKey(Module, null=True, on_delete= models.SET_NULL)
    Q = models.CharField(max_length=1000, null=False, blank=False)
    
    opt1 = models.CharField(max_length=200, null=False, blank=False)
    opt2 = models.CharField(max_length=200, null=False, blank=False)
    opt3 = models.CharField(max_length=200, null=True, blank=True)
    opt4 = models.CharField(max_length=200, null=True, blank=True)
    
    Correct = models.CharField(max_length=3, choices=(('1','1'),('2','2'),('3','3'),('4','4')))
    Reason = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Answer_Sheet(models.Model):
    Q = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    Result = models.ForeignKey(Result,null=True, blank=True, on_delete=models.CASCADE)
    right = models.BooleanField(default=False)
    Attempted_option = models.CharField(max_length=3, null=True, choices=(('1','1'),('2','2'),('3','3'),('4','4')))
    
    def __str__(self):
        return str(self.id)

#For now only
class i(models.Model):
    pass