from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from myapp.models import ConferenceModel,TalkModel,SpeakerModal,ParticipantModel

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = ConferenceModel
        fields = ['conference_title','conference_description','conference_start_date','conference_end_date']
        widgets = {
            'conference_title' : forms.TextInput(attrs={'class':'form-control '}),
            'conference_description' : forms.TextInput(attrs={'class':'form-control '}),
            'conference_start_date' : forms.DateField(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            'conference_end_date' : forms.DateField(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'})
        }

class TalkForm(forms.ModelForm):
    class Meta:
        model = TalkModel
        fields = ['talk_conference_title','talk_title','talk_description','talk_duration','talk_time']
        widgets = {
            'talk_conference_title' : forms.HiddenInput,
            'talk_title' : forms.TextInput(attrs={'class':'form-control '}),
            'talk_description' : forms.TextInput(attrs={'class':'form-control '}),
            'talk_duration' : forms.DecimalField(attrs={'class':'form-control '}),
            'talk_time' : forms.DateTimeField(attrs={'class':'form-control '}),
        }

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = SpeakerModal
        fields = ['speaker_talk_title','speaker_username','speaker_email']
        widgets = {
            'speaker_talk_title' : forms.HiddenInput, 
            'speaker_username' : forms.TextInput(attrs={'class':'form-control '}),
            'speaker_email' : forms.TextInput(attrs={'class':'form-control '})
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = ParticipantModel
        fields = ['participant_talk_title' , 'participant_username' , 'participant_email']
        widgets = {
            'participant_talk_title' : forms.HiddenInput,
            'participant_username' : forms.TextInput(attrs={'class':'form-control '}),
            'participant_email' : forms.TextInput(attrs={'class':'form-control '})
        }