from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Instructor, Course, Lesson


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email', 'specialty']

    def validate(self, attrs):
        instructor = Instructor(**attrs)

        try:
            instructor.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'title',
            'description', 'instructor',
            'start_date', 'end_date',
        ]

    def validate(self, attrs):
        course = Course(**attrs)

        try:
            course.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        return attrs


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'course', 'order']

    def validate(self, attrs):
        lesson = Lesson(**attrs)

        try:
            lesson.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        return attrs