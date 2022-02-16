import re
from django.shortcuts import render
from main.models import Participant, FirstExperiment, SecondExperiment, ThirdExperiment, FourthExperiment
import json
import glob
import random
import os

experiment_dirs = {
  1:'static/img/match/', 
  2:'static/img/unmatch/',
  3:'static/img/slight_match/',
  4:'static/img/slight_unmatch/',
}


def registration(request):

  if request.method == "GET" :
    return render(request, 'registration.html', context={'username':"", 'unregistered':True })

  else : 

    username = request.POST.get("username", "")
    username = username.lower()
    try : 
      participant = Participant(username=username)
      participant.save()    
      message = "Your username was set as " + username
      return render(request, 'registration.html', context={'username':message})
                                                           
    except Exception as e:
      message = "Your username is not acceptable"
      return render(request, 'registration.html', context={'username':message})
    

def experiment(request, experiment_id, username) :

  if request.method=="GET" : 

    if (experiment_id>4) or (experiment_id<1) :
      return render(request, 'error.html', context={'message':'Invalid Experiment ID!'})

    participant = Participant.objects.filter(username=username)
    if participant.count() == 0 : 
      return render(request, 'error.html', context={'message':'Could not find this user!'})
    else : 
      img_dir = experiment_dirs[experiment_id]
      im_path = random.sample(glob.glob(img_dir + '*.gif'), 1)[0]
      return render(request, 'experiment.html', context={'url':username, 
                                                  'image_path':'/'+im_path})
      

  if request.method=="POST" :

    reaction_time = int(json.loads(request.body)['reaction_time'])
    participant = Participant.objects.get(username=username)

    if experiment_id==1:
      participant.first_experiment = reaction_time 
    elif experiment_id==2:
      participant.second_experiment = reaction_time 
    elif experiment_id==3:
      participant.third_experiment = reaction_time 
    elif experiment_id==4:
      participant.fourth_experiment = reaction_time 
    else :
      return render(request, 'error.html', context={'message':'Something went wrong, you did not participate in any experiments!!'})
    
    participant.save()
    return render(request, 'experiment.html')




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