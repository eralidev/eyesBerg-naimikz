from rest_framework import viewsets
from .models import FeedbackModel, FAQsModel, FeedbackImageModel
from .serializers import FeedbackSerializer, FAQsSerializer, FeedbackImageSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer


class FAQsViewSet(viewsets.ModelViewSet):
    queryset = FAQsModel.objects.all()
    serializer_class = FAQsSerializer


class FeedbackImageViewSet(viewsets.ModelViewSet):
    queryset = FeedbackImageModel.objects.all()
    serializer_class = FeedbackImageSerializer
