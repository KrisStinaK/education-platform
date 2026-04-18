from django.db import models
from django.conf import settings
from courses.models import Course

class Certificate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    certificate_number = models.CharField(max_length=50, unique=True, blank=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"Сертификат {self.user.username} на курс {self.course.title}"

    def save(self, *args, **kwargs):
        if not self.certificate_number:
            # Генерация уникального номера сертификата
            self.certificate_number = f"{self.user.id}-{self.course.id}-{self.issue_date.strftime('%Y%m%d')}"
        super().save(*args, **kwargs)