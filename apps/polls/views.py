from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request,JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone 
import uuid


from .models import Election,Position,Candidate,AnonymousVoter


#prevents users from accessing webpage when not logged in
@login_required 
def election(request):
    lastest_election_list = Election.objects.all()
    context = {
        "lastest_election_list" : lastest_election_list,
        "title": "Home",
    }
    return render(request,'polls/election.html',context)


@login_required 
#Show and display Candidate-Postions
def positions(request, election_id):
    candidiate_postions = Position.objects.filter(election_id=election_id)
    election = get_object_or_404(Election,id=election_id)
    
    if election.end_date < timezone.now():
        return render(request,'polls/expire.html')
    elif election.start_date > timezone.now():
        return render(request,'polls/expire.html')

    if len(candidiate_postions)== 0:
        return render(request,"errors/page-404.html")
    context = {
        "position_list":candidiate_postions,
        "title": "Positions",
    }
    return render(request,'polls/position.html',context)

@login_required 
#Show and display Candidates
def candidates(request,position_id):
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

    if 'voter_id' not in request.session:
        # Generate a unique identifier for the voter
        voter_id = str(uuid.uuid4())
        request.session['voter_id'] = voter_id
    else:
        voter_id = request.session['voter_id']

    if Candidate.objects.filter(position_id=candidate.position_id, voters__identifier=voter_id).exists():
        return JsonResponse({'success': False, 'message': 'You have already voted for a candidate in this position'})
    

    # Check if the user has already voted for this candidate
    if not candidate.voters.filter(identifier=voter_id).exists():
        candidate.vote += 1 
        candidate.save()
        candidate.voters.add(AnonymousVoter.objects.create(identifier=voter_id))

        return JsonResponse({'success':True,'message':'You have voted successfully'})
    else:
        return JsonResponse({'success':False,'message':'You have already voted'})
