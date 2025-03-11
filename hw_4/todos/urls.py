from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("<int:id>/", views.todo_detail, name="todo_detail"),
    path("<int:id>/delete/", views.todo_delete, name="todo_delete"),
    path("<int:id>/edit/", views.todo_edit, name="todo_edit"),
    path("todos/<int:id>/delete/", views.task_delete, name="task_delete"),
    path("todos/<int:id>/edit/", views.task_edit, name="task_edit"),
]
