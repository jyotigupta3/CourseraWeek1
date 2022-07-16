from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, "polls/index.html", context)


def owner(request):
    return HttpResponse("Hello, world. ce697140 is the polls index.")


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     context = {"question": "You're looking at question %s." % question}
    #
    # except Exception as e:
    #     raise Http404("Question doesn't exist.", e)
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request=request, template_name="polls/detail.html", context=context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, "polls/detail.html",
                      context={'question': question, 'error_message': "you didn't select a choice. "})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
