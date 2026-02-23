from django.shortcuts import render



# Create your views here.
from .models import Question


def view_question(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        if question.answer == request.POST['Answer']:
            feedback = "Helyes válasz"
        else:
            feedback = "Helytelen válasz"
        selected = request.POST['Answer']

    else:
        feedback = None
        selected = None


    context = {
        'question': question,
        'feedback': feedback,
        'selected': selected
    }

    return render(request, 'app/hello.html', context)
