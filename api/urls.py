from django.urls import path
from . import views


urlpatterns = [
    path('instructors/', views.InstructorListCreateAPIView.as_view()),
    path('instructors/<int:pk>/', views.InstructorViewSet.as_view()),
    path('courses/', views.CourseListCreateAPIView.as_view()),
    path('courses/<int:pk>/', views.CourseViewSet.as_view()),
    path('lessons/', views.LessonListCreateAPIView.as_view()),
    path('lessons/<int:pk>/', views.LessonViewSet.as_view())
]