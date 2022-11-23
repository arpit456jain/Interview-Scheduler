from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class schedule(models.Model):
    id = models.AutoField(primary_key=True)
    interviewerName = models.CharField(max_length=100,blank=True)
    interviewerEmail = models.CharField(max_length=100,blank=True)
    intervieweeName = models.CharField(max_length=300,blank=True)
    intervieweeEmail = models.CharField(max_length=300,blank=True)
    allinterviewers = models.CharField(max_length=300,blank=True)
    intervieweStartTime = models.CharField(max_length=300,blank=True)
    intervieweEndTime = models.CharField(max_length=300,blank=True)
    interviewDate = models.CharField(max_length=300,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    


class candidates(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    candidate_name = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    interview_id = models.ForeignKey(schedule, on_delete=models.CASCADE)
