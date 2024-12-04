from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet, CourseViewSet, LessonViewSet

router = DefaultRouter()
router.register('instructors', InstructorViewSet, basename='instructor')
router.register('courses', CourseViewSet, basename='course')
router.register('lessons', LessonViewSet, basename='lesson')

urlpatterns = router.urls