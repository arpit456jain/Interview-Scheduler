from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class schedule(models.Model):
    interviewerName = models.CharField(max_length=100,blank=True)
    interviewerEmail = models.CharField(max_length=100,blank=True)
    intervieweeName = models.CharField(max_length=300,blank=True)
    intervieweeEmail = models.CharField(max_length=300,blank=True)
    allinterviewers = models.CharField(max_length=300,blank=True)
    intervieweStartTime = models.CharField(max_length=300,blank=True)
    intervieweEndTime = models.CharField(max_length=300,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)