from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Question, UserAnswer
from .serializers import QuestionSerializer, PracticeHistorySerializer
from rest_framework.permissions import IsAuthenticated


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionDetailView(APIView):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class SubmitAnswerView(APIView):
    def post(self, request, id, *args, **kwargs):
        question = get_object_or_404(Question, id=id)
        selected_answer = request.data.get('selected_answer')

        UserAnswer.objects.create(
            user=request.user,
            question=question,
            selected_answer=selected_answer
        )
        return Response({"message": "Answer submitted successfully."}, status=201)


class PracticeHistoryView(APIView):
    def get(self, request, user_id):
        answers = UserAnswer.objects.filter(user_id=user_id)
        serializer = PracticeHistorySerializer(answers, many=True)
        return Response(serializer.data)
