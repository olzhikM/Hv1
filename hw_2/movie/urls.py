from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),         # GET movies/
    path('<int:pk>/', views.movie_detail, name='movie_detail'),  # GET movies/:id
]
