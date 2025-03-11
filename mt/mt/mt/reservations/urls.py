from django.urls import path
from .views import reservation_update, reservation_delete, reservation_list, reservation_detail

urlpatterns = [
    path("", reservation_list, name="reservation_list"),
    path("<int:id>/", reservation_detail, name="reservation_detail"),
    path("<int:id>/upadate/", reservation_update, name="reservation_update"),
    path("<int:id>/delete/", reservation_delete, name="reservation_delete"),
]