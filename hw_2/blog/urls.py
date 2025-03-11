from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),       # GET articles/
    path('<int:pk>/', views.article_detail, name='article_detail'),  # GET articles/:id
]
