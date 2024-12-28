from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


from .models import Question

def landing(request):
    return render(request, 'landing.html')

def quiz_page(request):
    questions = Question.objects.prefetch_related('answers').all()
    return render(request, 'quiz.html', {'questions': questions})

from django.shortcuts import render, redirect


def result_page(request):
    if request.method == 'POST':
        score = 0
        total = 0

        # Retrieve and validate submitted answers
        submitted_answers = request.POST.dict()  # Convert QueryDict to a standard dictionary
        for question_id, answer_id in submitted_answers.items():
            if question_id.isdigit():  # Ensure the key is a question ID
                try:
                    question = Question.objects.get(id=question_id)
                    total += 1
                    if question.answers.get(id=answer_id).is_correct:
                        score += 1
                except (Question.DoesNotExist, question.answers.model.DoesNotExist):
                    continue

        # Redirect to the results page with score and total as query parameters
        return redirect(f'/results/?score={score}&total={total}')

    # If not a POST request, redirect back to the quiz page
    return redirect('quiz')

def results(request):
    score = request.GET.get('score', 0)
    total = request.GET.get('total', 0)
    return render(request, 'results.html', {'score': score, 'total': total})




