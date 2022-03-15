from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from questions.models import Question, Answer
from questions.api.serializers import QuestionSerializer
from questions.api.permissions import IsAuthorOrReadOnly

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    lookup_field = "slug"

    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)