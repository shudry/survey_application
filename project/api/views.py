#from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import SurveyModel, QuestionModel
from .serializers import (
        SurveySerializer, SurveySerializerWithoutStartDate, QuestionSerializer
    )

# Create your views here.

class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    serializer_class_no_change_start_date = SurveySerializerWithoutStartDate

    queryset = SurveyModel.objects.all()

    def get_serializer_class(self):
        ''' No change start date after create survey '''
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            # Show update form without start date field
            serializer_class = self.serializer_class_no_change_start_date

        return serializer_class

    @action(methods=['get'], detail=False)
    def active_surveys(self, request):
        return Response(SurveyModel.get_list_names_active_surveys())


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = QuestionModel.objects.all()
