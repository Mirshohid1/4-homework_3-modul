from django.db import models
from django.core.exceptions import ValidationError


def clean_field(
        value: str,
        field_name: str,
        title_case=False,
        min_length=3,
        skip_length_validation=False
):
    """
    Cleaner with validation.

    Args:
        value (str): The field value to clean.
        field_name (str): The field name for validation errors messages.
        title_case (bool): If True, converts the value to title case.
        min_length (int): Minimum length required for the value.
        skip_length_validation (bool): If True, skips length validation.

    Returns:
        str: cleaned value
    """

    if value:
        value = value.strip()
        if title_case:
            value = value.title()
        if len(value) < min_length and not skip_length_validation:
            raise ValidationError({
                field_name: f"The {field_name} must contain at least {min_length} characters."
            })

    return value

class Instructor(models.Model):

    SPECIALTY_CHOICES = [
        ('director', 'Director'),
        ('product_manager', 'Product Manager'),
        ('team_lead', 'Team Leader'),
        ('software_developer', 'Software Developer'),
        ('backend_programmer', 'Backend Programmer'),
        ('fronted_programmer', 'Fronted Programmer'),
        ('data_science', 'Data Science'),
        ('py_back_dev', 'Python Backend Development'),
        ('c#_back_dev', 'C# Backend Development'),
        ('java_back_dev', 'Java Backend Development'),
        ('designer', 'Designer'),
        ('operator', 'Operator'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    specialty = models.CharField(max_length=19, choices=SPECIALTY_CHOICES)

    def clean(self):
        """
        Validation and Data Processing
        """

        self.name = clean_field(self.name, 'name', title_case=True)
        self.email = clean_field(self.email, 'email', skip_length_validation=True)
        self.specialty = clean_field(self.specialty, 'specialty')

    def __str__(self):
        return f"{self.name} ({self.specialty})"


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')

    def clean(self):
        """
        Validation and Data Processing
        """

        self.title = clean_field(self.title, 'title', title_case=True)
        self.description = clean_field(self.description, 'description', min_length=12)

        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError({'end_date': "End date must be after the start date."})


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    order = models.IntegerField()

    def clean(self):
        """
        Validation and Data Processing
        """

        self.title = clean_field(self.title, 'title', title_case=True)
        self.content = clean_field(self.content, 'content', min_length=12)

        if self.order <= 0:
            raise ValidationError({'order': "The serial number must be positive."})
