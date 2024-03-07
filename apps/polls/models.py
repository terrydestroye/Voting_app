from django.db import models
from django.db import models
from django.utils import timezone
from apps.accounts.models import CustomUser

#Election class (to create multiple spaces 
#for elections that serve different purposes e.g prefects, staff voting etc

class Election(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    pub_date = models.DateTimeField('date published',default = timezone.now)
    status = models.CharField(max_length=20, default='Open')

    def __str__(self):
        return self.title
    
class Position(models.Model):
    #postion_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    position_description = models.TextField()
    election_id =models.ForeignKey(Election, on_delete = models.CASCADE)
    pub_date = models.DateTimeField('date published',default = timezone.now)    
    def __str__(self):
        return self.title
    
    
class Candidate(models.Model):
    #candidate_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position,on_delete=models.CASCADE)
    election_id = models.ForeignKey(Election,on_delete=models.CASCADE)
    short_manifesto = models.TextField(default ='pls vote for me bro!*insert sad face emoji')
    pub_date = models.DateTimeField('date published',default = timezone.now)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.student.username


class Votes(models.Model):
    #vote_id = models.AutoField(primary_key=True)
    election_id = models.ForeignKey(Election, on_delete=models.CASCADE)
    #student is a voter
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Vote for {self.candidate.name} by {self.voter.username}"
    

# Create your models here.

# Create your models here.
