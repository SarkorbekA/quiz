from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('questions/', views.random_question_list, name='random_question_list'),
    path('check-answers/', views.check_answers, name='check_answers'),
]