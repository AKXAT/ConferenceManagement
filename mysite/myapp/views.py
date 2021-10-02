from django.shortcuts import render
from django import forms
#from myapp.forms import ConferenceForm,TalkForm,SpeakerForm,ParticipantForm
from myapp.models import ConferenceModel,TalkModel,SpeakerModal,ParticipantModel
# Create your views here.

def conferenceView(request):
    conference = ConferenceModel.objects.all()
    return render(request,'myapp/conference.html',{'conference':conference})
