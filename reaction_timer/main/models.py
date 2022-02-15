from django.db import models


# Create your models here.

class Participant(models.Model) : 

  username = models.CharField(max_length=10, 
       unique=True, 
       blank=False, 
       null=False)

  first_experiment = models.IntegerField(default=0)
  second_experiment = models.IntegerField(default=0)
  third_experiment = models.IntegerField(default=0)
  fourth_experiment = models.IntegerField(default=0)

class FirstExperiment(models.Model) :

  paticipant = models.ForeignKey(Participant, on_delete=models.CASCADE)
  reaction_time = models.IntegerField()

  
class SecondExperiment(models.Model) :

  paticipant = models.ForeignKey(Participant, on_delete=models.CASCADE)
  reaction_time = models.IntegerField()



class ThirdExperiment(models.Model) :

  paticipant = models.ForeignKey(Participant, on_delete=models.CASCADE)
  reaction_time = models.IntegerField()



class FourthExperiment(models.Model) :

  paticipant = models.ForeignKey(Participant, on_delete=models.CASCADE)
  reaction_time = models.IntegerField()