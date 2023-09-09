from django import urls
from django.urls import path, include
from .views import (
    CourseListApiView,
    UserActivityListApiView,
    UserListApiView
)


urlpatterns = [
    path('courses/api/', CourseListApiView.as_view()),
    path('useractivity/api/', UserActivityListApiView.as_view()),
    path('user/api/', UserListApiView.as_view()),
]