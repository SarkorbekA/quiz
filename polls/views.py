import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question, Answer, Quiz
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError, NotFound
from django.core.exceptions import ObjectDoesNotExist
from random import shuffle


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title']


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'created_at', 'updated_at', 'answer_set']


class QuizSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['duration', 'question_count', 'question_set']


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET'])
def random_question_list(request):
    quiz = Quiz.objects.get(pk=1)

    questions = list(quiz.question_set.all())

    shuffle(questions)

    questions = questions[:quiz.question_count]

    question_serializer = QuestionSerializer(questions, many=True)

    quiz_data = QuizSerializer(quiz).data
    quiz_data['question_set'] = question_serializer.data

    return Response(quiz_data)


@api_view(['POST'])
def check_answers(request):
    data = json.loads(request.body)
    correct = 0
    no_correct = data['question_count'] - len(data['question_set'])
    for entry in data['question_set']:
        answer_id = entry.get('answer_id')
        try:
            answer = Answer.objects.get(id=answer_id)
            if answer.is_correct:
                correct += 1
            else:
                no_correct += 1
        except ObjectDoesNotExist:
            raise NotFound(
                {"error": "Answer with id {} not found".format(answer_id)},
            )

    return JsonResponse({'correct_count': correct, 'incorrect_count': no_correct})
