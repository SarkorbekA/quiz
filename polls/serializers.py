from rest_framework import serializers
from .models import Quizzes, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'title',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'id', 'title', 'answer',
        ]


class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = Quizzes
        fields = ['duration', 'question_count', 'question']
