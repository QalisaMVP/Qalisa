from rest_framework import serializers
from .models import Course, UserActivity, User, Lesson

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["course_name", "completed_lessons", "total_lessons", "course_category", "user"]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["lesson_name", "lesson_category", "user", "course"]


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields =["is_active", "last_login", "user"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["username", "email", "first_name", "last_name", "date_joined"]