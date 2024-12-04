from rest_framework import serializers
from .models import Instructor, Course, Lesson

import re


def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email', 'specialty']

    def validate_email(self, email):
        """
        Returns: If email is correct to return email.
        """

        if not is_valid_email(email):
            raise serializers.ValidationError("Enter the correct email address.")
        return email


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'title',
            'description', 'instructor',
            'start_date', 'end_date',
        ]

    def validate(self, attrs):
        """
        Checks that the end date is later than the start date.
        """
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("The end date must be later than the start date.")

        return attrs


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'course', 'order']

    def validate_order(self, order):
        """
        Checks if "order" is a positive number.
        """

        if order <= 0:
            raise serializers.ValidationError("The sequence number must be positive.")
