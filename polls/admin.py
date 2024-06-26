from django.contrib import admin
from . import models
from .models import Quizzes


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'title',
        'is_correct'
    ]
    extra = 4


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
        'date_updated'
    ]
    inlines = [
        AnswerInlineModel,
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        default_quiz = Quizzes.objects.get(pk=1)
        form.base_fields['quiz'].initial = default_quiz
        return form


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_correct',
        'question'
    ]
