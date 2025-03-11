from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login'), name='home'),  # Перенаправляем на /login/
    path('login/', include('django.contrib.auth.urls')),
    path('todos/', include('todos.urls')),
]
