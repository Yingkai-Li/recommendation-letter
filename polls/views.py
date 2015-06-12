from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms

from .models import Choice, Question, Choiceship
from django.contrib.auth.decorators import login_required

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

'''
@login_required
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        new_choice = Choiceship(request.user.username, 1)
        new_choice.save()
        selected_choice.members.add(new_choice)
        #selected_choice.members.add(request.user)
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''

class ChoiceForm(forms.Form):
    choice = forms.CharField()
    score = forms.IntegerField()

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    #form = ChoiceForm(request.POST)
    for selected_choice in p.choice_set.all():
        for score_choice in selected_choice.members.all():
            username = score_choice.student
            if (username == request.user.username):
                selected_choice.members.remove(score_choice)
                #score_choice.delete()
                selected_choice.votes -= 1
        new_choice = Choiceship.create(request.user.username, request.POST[selected_choice.choice_text])
        new_choice.save()
        selected_choice.members.add(new_choice)
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))