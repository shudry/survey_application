from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SurveyViewSet, QuestionViewSet, ActiveSurveysListView


router = DefaultRouter()
router.register(r'administrator/surveys', SurveyViewSet, basename='survey')
router.register(r'administrator/questions', QuestionViewSet, basename='question')

# Formatting djangorest urls in django paths.
urlpatterns = [
    path(r'list-active-surveys/', ActiveSurveysListView.as_view()),
] + router.urls
