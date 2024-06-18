from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.IntegerField()
    msg = models.TextField()
    mark = models.IntegerField()
    created_at = models.DateField()
    # service = models.ForeignKey('Service', related_name='comments', on_delete=models.CASCADE)
    service = models.IntegerField()

    def __str__(self):
        return f'Comment {self.id} on Service {self.service}'


class CommentImage(models.Model):
    image = models.CharField(max_length=255)
    comment = models.ForeignKey(Comment, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'CommentImage {self.id} for Comment {self.comment}'


class QuestionAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    role = models.CharField(max_length=255)

    def __str__(self):
        return f'QuestionAnswer {self.id}'
