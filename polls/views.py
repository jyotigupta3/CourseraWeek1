from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, "polls/index.html", context)


def owner(request):
    return HttpResponse("Hello, world. ce697140 is the polls index.")


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {"question": "You're looking at question %s." % question}

    except Exception as e:
        raise Http404("Question doesn't exist.", e)

    return render(request=request, context=context, template_name="polls/detail.html")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
