from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
        context = {"question": question}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    context = {"response": "You're looking at the results of question",
               "question_id": question_id}
    return render(request, "polls/results.html", context)


def vote(request, question_id):
    context = {"response": "You're voting on question",
               "question_id": question_id}
    return render(request, "polls/vote.html", context)
