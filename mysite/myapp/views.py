from django.shortcuts import render
from django import forms
from myapp.forms import ConferenceForm,TalkForm,SpeakerForm,ParticipantForm
from myapp.models import ConferenceModel,TalkModel,SpeakerModal,ParticipantModel
# Create your views here.

def conferenceView(request):
    if request.method == 'POST':
        conferenceform = ConferenceForm(request.POST)
        if conferenceform.is_valid():
            conferenceform.save()
            conferenceform = ConferenceForm()  
    else:
        conferenceform = ConferenceForm()
    conference = ConferenceModel.objects.all()
    return render(request,'myapp/conference.html',{'conference':conference,'conferenceform':conferenceform})
