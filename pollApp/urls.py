from django.urls import path
from .import views 

app_name = 'pollApp'
urlpatterns = [
    path('election/',views.election, name = 'election'),
    path('position/<int:election_id>',views.positions, name = 'position'),
    path('candidate/<int:position_id>',views.candidates, name = 'candidate'),
]