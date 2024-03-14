from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request,JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone 



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

    user_ip = request.META.get('REMOTE_ADDR', None)
    browser_info = request.META.get('HTTP_USER_AGENT', None)
    timestamp = timezone.now()

    # Check if the user has already voted for this candidate
    if not candidate.voters.filter(ip_address=user_ip).exists():
        voter = AnonymousVoter.objects.create(timestamp=timestamp)
        candidate.voters.add(voter)
        candidate.vote += 1
        candidate.save()

        return JsonResponse({'success':True,'message':'You have voted successfully'})
    else:
        return JsonResponse({'success':False,'message':'You have already voted'})
