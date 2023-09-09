from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    Course,
    UserActivity
)


admin.site.register(User, UserAdmin)


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'completed_lessons', 'total_lessons', 'course_category', 'user']


@admin.register(UserActivity)
class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ['is_active', 'last_login', 'user']