from django.shortcuts import render
from django import forms
from django.shortcuts import render,HttpResponsePermanentRedirect,HttpResponse
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

def conferenceedit(request,id):
    if request.method == 'POST':
        uniqueconferencetitle = ConferenceModel.objects.get(pk=id)
        requestconferencedetails = ConferenceForm(request.POST,instance=uniqueconferencetitle)
        if requestconferencedetails.is_valid():
            requestconferencedetails.save()
            return HttpResponsePermanentRedirect('/')
    else:
        uniqueconferencetitle = ConferenceModel.objects.get(pk=id)
        requestconferencedetails = ConferenceForm(instance=uniqueconferencetitle)
    return render(request,'myapp/conferenceedit.html',{'requestconferencedetails':requestconferencedetails})
    

def conferencedelete(request,id):
    if request.method == 'POST':
        conferencedelete = ConferenceModel.objects.get(pk=id)
        conferencedelete.delete()
        return HttpResponsePermanentRedirect('/')