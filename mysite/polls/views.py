from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers

from .models import Choice, Question

def index(request):
    return render(request, 'polls/index.html', {})

def list2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    result = list(latest_question_list)
    serialized_obj = serializers.serialize('json', result)
    return HttpResponse(serialized_obj, content_type = "application/json")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serialized_obj = serializers.serialize('json', [question])
    return HttpResponse(serialized_obj, content_type = "application/json")

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serialized_obj = serializers.serialize('json', list(question.choice_set.all()))
    return HttpResponse(serialized_obj, content_type = "application/json")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        raise Http404("You didn't select a choice.")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
