from rest_framework import serializers
from .models import Question, UserAnswer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']


class PracticeHistorySerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.text')

    class Meta:
        model = UserAnswer
        fields = ['question_id', 'question_text', 'selected_answer', 'created_at']
