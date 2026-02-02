from django.shortcuts import render



# Create your views here.
from .models import Question


def view_question(request, question_id):
    question = Question.objects.get(id=question_id)

    context = {
        'question': question
    }

    return render(request, 'app/hello.html', context)
