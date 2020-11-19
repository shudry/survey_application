from django.db import models
from django.template.defaultfilters import date as _date

# Create your models here.

class SurveyModel(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(null=True, blank=True)

    datetime_start = models.DateTimeField(auto_now_add=True)
    datetime_end = models.DateTimeField(auto_now_add=True)

    @property
    def formated_datetime_start(self):
        ''' Field datetime_start contain datetime in format like this
            2008-01-02T10:30:00.000123+02:00

            Formatting to readable format by _date function.

            For the full list format characters, see
            https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date
        '''
        return _date(self.datetime_start, 'j E Y (H:i)')

    @property
    def formated_datetime_end(self):
        ''' Field datetime_end contain datetime in format like this
            2008-01-02T10:30:00.000123+02:00

            Formatting to readable format by _date function.

            For the full list format characters, see
            https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date
        '''
        return _date(self.datetime_end, 'j E Y (H:i)')

    @property
    def dates_info(self):
        return 'Start survey {}. End {}'.format(self.formated_datetime_start,
                                                self.formated_datetime_end)

    @property
    def questions(self):
        return self.related_question.all()


class QuestionModel(models.Model):
    survey = models.ForeignKey(SurveyModel, on_delete=models.CASCADE,
                               related_name='related_question')
    text = models.TextField()

    @property
    def choices(self):
        return self.related_choice.all()


class ChoiceOptionModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE,
                                 related_name='related_choice')

    choice_text = models.CharField(max_length=300)
