# from core import settings
from django.urls import path
from .import views

# from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    path('',views.election, name = 'election'),
    path('position/<int:election_id>/',views.positions, name = 'position'),
    path('candidate/<int:position_id>/',views.candidates, name = 'candidate'),
    path('votes/<int:candidate_id>/',views.vote_view, name = 'voter_view'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)