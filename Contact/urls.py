from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("del/<str:pk>", views.delete, name="delete"),
    path("login", views.login, name="login"),
]
