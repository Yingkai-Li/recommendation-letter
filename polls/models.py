from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text
        
class Choiceship(models.Model):
    #choice = models.ForeignKey(Choice)
    student = models.CharField(max_length=200, default="")
    score = models.IntegerField(default=0)
    
    @classmethod
    def create(cls, student, score):
        choice = cls(student=student, score=score)
        # do something with the book
        return choice
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.student + ':' + str(self.score)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    members = models.ManyToManyField(Choiceship, related_name='selection', default = None)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text
       
