from django.db import models

class Candidate(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=254,default=False)
  user_id =models.CharField(max_length=254,default=False)
  start_time = models.DateTimeField('Start time',default=False)
  end_time = models.DateTimeField('End time',default=False)
  class Meta:
    ordering = ['start_time']

