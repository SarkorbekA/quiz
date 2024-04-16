from django.db import models
from django.utils.translation import gettext_lazy as _


class Quizzes(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    id = models.BigAutoField(primary_key=True)
    duration = models.IntegerField()
    question_count = models.IntegerField()
    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    id = models.BigAutoField(primary_key=True)
    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))

    def __str__(self):
        return self.title


class Answer(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    title = models.CharField(
        max_length=255, verbose_name=_("Answer Title"))
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title
