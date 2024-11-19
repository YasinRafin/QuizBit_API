from django.urls import path
from .views import (
    QuestionListView,
    QuestionDetailView,
    SubmitAnswerView,
    PracticeHistoryView,
)

urlpatterns = [
    path("questions/", QuestionListView.as_view(), name="question-list"),
    path("questions/<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
    path('questions/<int:id>/submit/', SubmitAnswerView.as_view(), name='submit_answer'),
    path(
        "users/<int:user_id>/history/",
        PracticeHistoryView.as_view(),
        name="practice-history",
    ),
]
