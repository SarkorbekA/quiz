import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Answer, Quizzes
from .serializers import QuizSerializer, QuestionSerializer
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from random import shuffle
from django.utils import timezone
from datetime import timedelta


@api_view(['GET'])
def random_question_list(request):
    quiz = Quizzes.objects.get(pk=1)

    questions = list(quiz.question.all())

    shuffle(questions)

    questions = questions[:quiz.question_count]

    question_serializer = QuestionSerializer(questions, many=True)

    quiz_data = QuizSerializer(quiz).data

    current_time = timezone.now()

    quiz_data['question'] = question_serializer.data
    quiz_data['start_at'] = current_time
    quiz_data['end_at'] = current_time + timedelta(minutes=quiz_data['duration'])

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
