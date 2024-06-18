from rest_framework import serializers
from .models import Comment, QuestionAnswer, CommentImage


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImage
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'
