from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Answer, Result
from courses.models import Lesson
from .forms import QuizForm, QuestionForm, AnswerForm
from .forms import AnswerForm

@login_required
def quiz_list(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {
        'quizes': quizes})


@login_required
def quiz_create(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        form_answer = QuestionForm(request.POST)
        if form.is_valid() and form_answer.is_valid():
            form_answer.save(commit=False)
            quiz = form.save(commit=False)
            quiz.lesson = lesson
            quiz.save()
            return redirect('quizzes:quiz_detail', quiz_id=quiz.id)
    else:
        form = QuizForm()
        form_answer = QuestionForm()
    return render(request, 'quiz/quiz_create.html', {'form': form,
                                                     'form_a': form_answer,
                                                       'lesson': lesson})

@login_required
def start_test(request, quiz_id):
    test = get_object_or_404(Quiz, pk=quiz_id)
    questions = test.questions.all()
    if request.method == 'POST':
        form = AnswerForm(questions, request.POST)
        if form.is_valid():
            score = 0
            for question in questions:
                selected_answer_id = int(form.cleaned_data[f'question_{question.id}'])
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1
            # Сохраняем результат
            Result.objects.create(
                user=request.user,
                test=test,
                score=score,
                total_questions=questions.count()
            )
            context = {
                'score': score,
                'total': questions.count(),
            }
            return render(request, 'quiz/result.html', context)
    else:
        form = AnswerForm(questions)
    return render(request, 'quiz/quiz_detail.html', {'form': form,
                                                      'test': test, 'questions': questions})

@login_required
def results_history(request):
    results = Result.objects.filter(user=request.user).select_related('test').order_by('-date_taken')
    return render(request, 'quiz/results_history.html', {'results': results})