from rest_framework import serializers
from .models import Instructor, Course, Lesson
from .mixins import ModelValidationMixin


class InstructorSerializer(ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email', 'specialty']


class CourseSerializer(ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'title',
            'description', 'instructor',
            'start_date', 'end_date',
        ]


class LessonSerializer(ModelValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'course', 'order']
