from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

urlpatterns = [
    path('', index, name='index'),  # ← добавьте главную страницу
    path('admin/', admin.site.urls),
    path('api/', include('movie.urls')),
    path('api/', include('blog.urls')),
]
