from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

#Election class (to create multiple voting spaces)
#for elections that serve different purposes e.g prefects, staff voting etc
class Election(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    pub_date = models.DateTimeField('date published',default = timezone.now)

    def __str__(self):
        return self.title
    
class Position(models.Model):
    title = models.CharField(max_length=300)
    position_description = models.TextField()
    election_id =models.ForeignKey(Election, on_delete = models.CASCADE)
    pub_date = models.DateTimeField('date published',default = timezone.now)    
    def __str__(self):
        return self.title

class AnonymousVoter(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)  
    
    def __str__(self):
        return f"Vote from {self.ip_address} at {self.timestamp}"
    
class Candidate(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position,on_delete=models.CASCADE)
    election_id = models.ForeignKey(Election,on_delete=models.CASCADE)
    voters = models.ManyToManyField(AnonymousVoter, related_name='voters',blank=True)
    short_manifesto = models.TextField(default ='Vote for me')
    pub_date = models.DateTimeField('date published',default = timezone.now)
    profile_picture = models.ImageField(default='Default.jpg',upload_to='profile_pictures/')
    vote = models.IntegerField(default=0)
    
    def __str__(self):
        return self.student.username