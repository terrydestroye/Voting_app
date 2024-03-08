from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, request
from django.template import loader
from django.urls import reverse ## write the reverse function yourself
from django.contrib.auth.decorators import login_required

from .models import Election,Position,Candidate,Votes


#prevents users from accessing webpage when not logged in
@login_required 
def election(request):
    # lastest_election_list = Election.objects.all()
    context = {
        #'elections': elections,
        "lastest_election_list" : Election.objects.all(),
        "title": "Home",
    }
    return render(
        request, 
        'polls/election.html',
        context 
    )

#Show and display Candidate-Postions
@login_required 
def positions(request, election_id):
    #position_list = Position.objects.order_by('-pub_date')
    candidiate_postions = Position.objects.filter(election_id=election_id)
    if len(candidiate_postions)== 0:
        return render(request,"errors/page-404.html")
    context = {
        "position_list":candidiate_postions,
        "title": "Positions",
    }
    return render(request,'polls/position.html',context)


#Show and display Candidates
@login_required 
def candidates(request,position_id):
    #candidate_list = Candidate.objects.order_by('-pub_date')
    #candidate_list = [ candidate ]
    candidate_list = Candidate.objects.filter(position_id=position_id)

    if len(candidate_list)== 0:
        return render(request,"errors/page-404.html")
    
    context = {
        "candidate_list":candidate_list,
        "title": "Candidates",
    }
    return render(request,'polls/candidate.html',context)


def vote_view(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    voter = request.user  # Assuming you have a user system

    # Check if the user has already voted for this position
    if not Votes.objects.filter(voter=voter, position=candidate.position).exists():
        # Create a vote object and save it to the database
        vote = Votes(voter=voter, position=candidate.position, candidate=candidate)
        vote.save()

# function to vote for candidates
# def Vo






# Create your views here.
