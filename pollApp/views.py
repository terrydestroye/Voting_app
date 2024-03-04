from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, request
from django.template import loader
from django.urls import reverse ## write the reverse function yourself
from django.contrib.auth.decorators import login_required

from .models import Election,Position,Candidate


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
        '/home/playground/Desktop/django-coreui/apps/templates/pollApp/election.html',
        context 
    )

#Show and display Candidate-Postions
@login_required 
def positions(request, election_id):
    #position_list = Position.objects.order_by('-pub_date')
    candidiate_postions = Position.objects.filter(election_id=election_id)
    if len(candidiate_postions)== 0:
        return render(request,"/home/playground/Desktop/django-coreui/apps/templates/home/page-404.html")
    context = {
        "position_list":candidiate_postions,
        "title": "Positions",
    }
    return render(
        request,'/home/playground/Desktop/django-coreui/apps/templates/pollApp/position.html',context)


#Show and display Candidates
@login_required 
def candidates(request,position_id):
    #candidate_list = Candidate.objects.order_by('-pub_date')
    #candidate_list = [ candidate ]
    candidate = Candidate.objects.filter(position_id=position_id)

    if len(candidate)== 0:
        return render(request,"/home/playground/Desktop/django-coreui/apps/templates/home/page-404.html")
    
    context = {
        "candidate_list":candidate,
        "title": "Candidates",
    }
    return render(request,'/home/playground/Desktop/django-coreui/apps/templates/pollApp/candidate.html',context)

# function to vote for candidates
# def Vo






# Create your views here.
