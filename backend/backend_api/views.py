from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Course, UserActivity, User
from .serializers import CourseSerializer, UserActivitySerializer, UserSerializer, LessonSerializer

class CourseListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the course items for given requested user
        '''
        courses = Course.objects.filter(user = request.user.id)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Course with given course data
        '''
        data = {
            'course_name': request.data.get('course_name'), 
            'completed_modules': request.data.get('completed_lessons'), 
            'user': request.user.id
        }
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LessonListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the lesson items for given requested user
        '''
        lessons = Lesson.objects.filter(user = request.user.id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Course with given course data
        '''
        data = {
            'lesson_name': request.data.get('lesson_name'), 
            'user': request.user.id,
            'course': request.course.id
        }
        serializer = LessonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserActivityListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the activity for given requested user
        '''
        user_activity = UserActivity.objects.filter(user = request.user.id)
        serializer = UserActivitySerializer(user_activity)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the activity for given requested user
        '''
        username = User.objects.filter(user = request.user.id)
        serializer = UserSerializer(username)
        return Response(serializer.data, status=status.HTTP_200_OK)
