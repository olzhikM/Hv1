from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def redirect_to_threads(request):
    # Перенаправляет на маршрут 'thread_list' (который объявлен в post/urls.py)
    return redirect('thread_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('threads/', include('post.urls')),  # Подключаем маршруты приложения
    path('', redirect_to_threads, name='home'),  # Это перенаправление с '/'
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)