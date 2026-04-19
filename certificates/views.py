from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Certificate
from courses.models import Course, Enrollment
from django.http import HttpResponse


@login_required
def issue_certificate(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()

    if not enrollment:
        return HttpResponse("Вы не записаны на этот курс.")

    certificate, created = Certificate.objects.get_or_create(
        user=request.user, course=course
    )

    return render(
        request, "certificates/certificate_detail.html", {"certificate": certificate}
    )


@login_required
def certificate_detail(request, certificate_number):
    certificate = get_object_or_404(
        Certificate, certificate_number=certificate_number, user=request.user
    )
    return render(
        request, "certificates/certificate_detail.html", {"certificate": certificate}
    )
