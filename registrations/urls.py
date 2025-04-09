from django.urls import path
from . import views

urlpatterns = [
    path("", views.register_student, name="register"),
    path("success/", views.success, name="success"),
    path("registrations/", views.registrations_list, name="registrations_list")
]
