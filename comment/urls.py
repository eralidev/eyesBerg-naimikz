from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, QuestionAnswerViewSet, CommentImageViewSet

router = DefaultRouter()

router.register(r'comments', CommentViewSet)
router.register(r'question-answers', QuestionAnswerViewSet)
router.register(r'comment-images', CommentImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
