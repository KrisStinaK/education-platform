from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),
    path('profile/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('quizzes/', include('quizzes.urls', namespace='quizzes')),
    path('certificates/', include('certificates.urls', namespace='certificates')),
    path('', include('courses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)