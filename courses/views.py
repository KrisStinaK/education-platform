from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.db.models import Q
from .models import Course, Lesson, Enrollment
from .forms import LessonUpdateForm

class CourseCreateView(CreateView): # новое изменение
    model = Course
    template_name = 'courses/course_create.html'
    fields = ['title', 'description']

def home(request):
    courses = Course.objects.filter(is_active=True)
    return render(request,"courses/home.html", {'courses':courses[:5]})

@login_required
def course_list(request):
    courses = Course.objects.filter(is_active=True)
    query = request.GET.get('q')
    if query:
        courses = courses.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    # Проверка записей пользователя
    user_enrollments = Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True)
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'user_enrollments': user_enrollments,
        'query': query,
    })

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    lessons = course.lessons.filter(is_published=True)

    # Проверка записи
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()

    if request.method == 'POST':
        if not enrollment:
            Enrollment.objects.create(user=request.user, course=course)
            messages.success(request, 'Вы успешно записались на курс!')
        return redirect('courses:course_detail', pk=pk)

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'enrollment': enrollment,
    })

@login_required
def lesson_detail(request, course_id, lesson_id):
    course = get_object_or_404(Course, pk=course_id, is_active=True)
    lesson = get_object_or_404(Lesson, pk=lesson_id, course=course, is_published=True)

    # Проверка записи на курс
    enrollment = Enrollment.objects.filter(
        user=request.user, 
        course=course
    ).first()

    if not enrollment:
        messages.error(request, 'Сначала запишитесь на курс!')
        return redirect('courses:course_detail', pk=course_id)

    return render(request, 'courses/lesson_detail.html', {
        'course': course,
        'lesson': lesson,
        'enrollment': enrollment,
    })

@login_required
def lesson_delete_view(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, f'Урок успешно удален.')
        return redirect("courses:home")
    context = {'lesson': lesson, 'course': course}
    return render(request, 'courses/course_detail.html', context)


@login_required
def edit_lesson_view(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == 'GET':
        form = LessonUpdateForm(instance=lesson)
    elif request.method == 'POST':
        form = LessonUpdateForm(request.POST, instance=lesson)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Урок успешно обновлен.')
            return redirect('courses:course_list')

    else:
        form = LessonUpdateForm()

    context = {
        'form': form,
        'lesson': lesson,
        'course': course
    }
    return render(request, 'courses/lesson_edit.html', context)

@login_required
def create_lesson_view(request):
    if request.method == 'POST':
        form = LessonUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Урок успешно добавлен.')
            return redirect('courses:course_list')

    else:
        form = LessonUpdateForm()

    context = {
        'form': form,
    }
    return render(request, 'courses/lesson_edit.html', context)