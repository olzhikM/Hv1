from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('<int:id>/', views.thread_detail, name='thread_detail'),  # ВАЖНО!
]
