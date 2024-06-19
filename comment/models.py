from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FeedbackModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.IntegerField()
    msg = models.TextField()
    mark = models.IntegerField()
    created_at = models.DateField()
    service = models.IntegerField()

    def __str__(self):
        return f'Comment {self.pk} on Service {self.service}'

    class Meta:
        db_table = "feedback"


class FeedbackImageModel(models.Model):
    image = models.ImageField(upload_to='static/FeedbackImage/')
    comment = models.ForeignKey(FeedbackModel, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'CommentImage {self.pk} for Comment {self.comment}'

    class Meta:
        db_table = "FeedbackImage"


class FAQsModel(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'QuestionAnswer {self.pk}'

    class Meta:
        db_table = "FAQs"
