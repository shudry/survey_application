import json

from django.conf import settings
from rest_framework import serializers

from .models import SurveyModel, QuestionModel, ChoiceOptionModel


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOptionModel
        fields = ('choice_text', )


class QuestionSerializer(serializers.ModelSerializer):
    #choices = serializers.SerializerMethodField('get_choices')
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = QuestionModel
        fields = ('text', 'choices', )

    def get_choices(self, instance):
        serializer = ChoiceSerializer(instance.choices, many=True)
        return serializer.data

    def create(self, validated_data):
        choices = validated_data.pop('choices', None)

        question_instance = self.Meta.model.objects.create(**validated_data)

        if choices:
            choices_serializer = ChoiceSerializer(data=choices, many=True)
            if not choices_serializer.is_valid():
                return choices_serializer.errors

            choices_serializer.save(question_id=question_instance.id)

        return QuestionSerializer(question_instance).data


class SurveySerializer(serializers.ModelSerializer):
    #questions = serializers.SerializerMethodField('get_questions')
    questions = QuestionSerializer(many=True)

    datetime_start = serializers.DateTimeField(required=False)
    datetime_end = serializers.DateTimeField()

    class Meta:
        model = SurveyModel
        fields = ('id', 'name', 'description', 'datetime_start', 'datetime_end',
                  'questions', )

    def get_questions(self, instance):
        serializer = QuestionSerializer(instance.questions, many=True)
        return serializer.data

    def create(self, validated_data):
        questions = validated_data.pop('questions', None)

        survey_instance = self.Meta.model.objects.create(**validated_data)

        if questions:
            questions_serializer = QuestionSerializer(data=questions, many=True)
            if not questions_serializer.is_valid():
                return questions_serializer.errors

            questions_serializer.save(survey_id=survey_instance.id)

        return SurveySerializer(survey_instance).data


class SurveySerializerWithoutStartDate(serializers.ModelSerializer):
    datetime_end = serializers.DateTimeField(required=False)

    class Meta:
        model = SurveyModel
        fields = ('id', 'name', 'description', 'datetime_end')
