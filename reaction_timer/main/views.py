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
    participant.first_experiment = reaction_time
    participant.save()
    return render(request, 'first_experiment.html')
  
def second_experiment(request, username) : 

  if request.method=="GET" : 
    return render(request, 'second_experiment.html', context={'url':username})

  if request.method=="POST" :
    reaction_time = int(json.loads(request.body)['reaction_time'])
    participant = Participant.objects.get(username=username)
    participant.second_experiment = reaction_time
    participant.save()
    return render(request, 'second_experiment.html')

def third_experiment(request, username) : 

  if request.method=="GET" : 
    return render(request, 'third_experiment.html', context={'url':username})

  if request.method=="POST" :
    reaction_time = int(json.loads(request.body)['reaction_time'])
    participant = Participant.objects.get(username=username)
    participant.third_experiment = reaction_time
    participant.save()
    return render(request, 'third_experiment.html')

def fourth_experiment(request, username) : 

  if request.method=="GET" : 
    return render(request, 'fourth_experiment.html', context={'url':username})

  if request.method=="POST" :
    reaction_time = int(json.loads(request.body)['reaction_time'])
    participant = Participant.objects.get(username=username)
    participant.fourth_experiment = reaction_time
    participant.save()
    # FourthExperiment.objects.get_or_create(paticipant=participant, reaction_time=reaction_time)
    return render(request, 'fourth_experiment.html')

def results(request) : 

  participants = Participant.objects.all()

  results = { 'username' : [],
              'first_experiment' : [],
              'second_experiment' : [],
              'third_experiment' : [], 
              'fourth_experiment' : []}

  for participant in participants : 

    results['username'].append(participant.username)
    results['first_experiment'].append(participant.first_experiment)
    results['second_experiment'].append(participant.second_experiment)
    results['third_experiment'].append(participant.third_experiment)
    results['fourth_experiment'].append(participant.fourth_experiment)

  print(results['username'])
  print(type(results['username'][0]))
  print(type(results['first_experiment'][0]))
  print(type(results['second_experiment'][0]))
  print(type(results['third_experiment'][0]))
  print(type(results['fourth_experiment'][0]))

  print(json.dumps(results))

  return render(request, 'results.html', context={'results':json.dumps(results)})