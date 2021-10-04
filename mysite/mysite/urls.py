"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.conferenceView,name='conference'),
    path('delete/<str:id>',views.conferencedelete,name='conferencedelete'),
    path('<str:id>/edit',views.conferenceedit,name='conferenceedit'),
    path('<str:id>/talks/',views.talkView,name='talks'),
    path('delete/talk/<str:id>',views.talkdelete,name='talkdelete'),
    path('<str:id>/talks/edit',views.talkedit,name='talkedit'),
    path('admin/', admin.site.urls),
]
