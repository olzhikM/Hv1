from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # <-- Добавляем redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect("todo_list")),  # <-- Перенаправление на список TodoList
    path("todo-lists/", include("todos.urls")),
]
