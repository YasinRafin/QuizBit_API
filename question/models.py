from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    choices = models.JSONField()
    correct_answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"
