from django.db import models


# Create your models here.
class Quiz(models.Model):
    duration = models.IntegerField()
    question_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Quiz {self.id}"


class Question(models.Model):
    title = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Question {self.id}"


class Answer(models.Model):
    title = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def clean(self):
        answers_count = Answer.objects.filter(question=self.question).count()
        if answers_count >= 4:
            raise ValueError('Максимальное количество ответов для вопроса - 4.')