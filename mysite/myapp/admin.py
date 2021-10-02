from django.contrib import admin
from myapp.models import ConferenceModel,TalkModel,SpeakerModal,ParticipantModel

admin.site.register(ConferenceModel)
admin.site.register(TalkModel)
admin.site.register(SpeakerModal)
admin.site.register(ParticipantModel)
# Register your models here.
