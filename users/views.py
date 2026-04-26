from django.shortcuts import render,  redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import ProfileUpdateForm, UserUpdateForm
from courses.models import Enrollment, Course
from django.contrib import messages


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def profile_view(request):
    courses = Course.objects.filter(is_active=True)
    completed_courses = Enrollment.objects.filter(is_completed=True)
    user_enrollments = Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True)
    context = {'user_enrollments': user_enrollments,
               'active_courses': len(user_enrollments),
               'courses': courses,
               'completed_courses': len(completed_courses)}
    return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/edit_profile.html', context)