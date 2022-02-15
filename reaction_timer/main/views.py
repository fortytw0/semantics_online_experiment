import re
from django.shortcuts import render
from main.models import Participant, FirstExperiment, SecondExperiment, ThirdExperiment, FourthExperiment
import json


def registration(request):

  if request.method == "GET" :
    return render(request, 'registration.html', context={'username':""})

  else : 

    username = request.POST.get("username", "")
    try : 
      participant = Participant(username=username)
      participant.save()
      return render(request, 'registration.html', context={'username':"Your username was set as " + username})
    except Exception as e:
      return render(request, 'registration.html', context={'username':"Your username is not acceptable"})
    


def first_experiment(request, username) : 

  if request.method=="GET" : 
    return render(request, 'first_experiment.html', context={'url':username})

  if request.method=="POST" :
    reaction_time = int(json.loads(request.body)['reaction_time'])
    participant = Participant.objects.get(username=username)
    FirstExperiment.objects.get_or_create(paticipant=participant, reaction_time=reaction_time)
    return render(request, 'first_experiment.html')
  
def second_experiment(request, username) : 

  if request.method=="GET" : 
    return render(request, 'second_experiment.html', context={'url':username})

  if request.method=="POST" :
    reaction_time = int(json.loads(request.body)['reaction_time'])
    participant = Participant.objects.get(username=username)
    SecondExperiment.objects.get_or_create(paticipant=participant, reaction_time=reaction_time)
    return render(request, 'second_experiment.html')

def third_experiment(request, username) : 

  if request.method=="GET" : 
    return render(request, 'third_experiment.html', context={'url':username})

  if request.method=="POST" :
    reaction_time = int(json.loads(request.body)['reaction_time'])
    participant = Participant.objects.get(username=username)
    ThirdExperiment.objects.get_or_create(paticipant=participant, reaction_time=reaction_time)
    return render(request, 'third_experiment.html')

def fourth_experiment(request, username) : 

  if request.method=="GET" : 
    return render(request, 'fourth_experiment.html', context={'url':username})

  if request.method=="POST" :
    reaction_time = int(json.loads(request.body)['reaction_time'])
    participant = Participant.objects.get(username=username)
    FourthExperiment.objects.get_or_create(paticipant=participant, reaction_time=reaction_time)
    return render(request, 'fourth_experiment.html')

def results(request) : 

  first_experiment_reaction_times = FirstExperiment.objects.all()


  return render(request, 'results.html', context={
    'first_experiment':first_experiment_reaction_times
  })