from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("judge/", views.judge, name="judge"),
    path("new_target/", views.new_target, name="new_target"),
]
