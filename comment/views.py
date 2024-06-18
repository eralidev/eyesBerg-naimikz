from rest_framework import viewsets
from .models import Comment, QuestionAnswer, CommentImage
from .serializers import CommentSerializer, QuestionAnswerSerializer, CommentImageSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer


class CommentImageViewSet(viewsets.ModelViewSet):
    queryset = CommentImage.objects.all()
    serializer_class = CommentImageSerializer
