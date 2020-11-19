from rest_framework.routers import DefaultRouter

from .views import SurveyViewSet, QuestionViewSet


router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='survey')
router.register(r'questions', QuestionViewSet, basename='question')

# Formatting djangorest urls in django paths.
urlpatterns = router.urls
