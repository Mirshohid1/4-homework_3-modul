from rest_framework.viewsets import ModelViewSet
from .models import Instructor, Course, Lesson
from .serializers import InstructorSerializer, CourseSerializer, LessonSerializer


class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer