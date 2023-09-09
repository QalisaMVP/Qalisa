from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Course(models.Model):
    course_name = models.CharField(max_length=150)
    completed_lessons = models.IntegerField(default=0)
    total_lessons = models.IntegerField()
    course_category = models.CharField(max_length=40)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.course_name
    

class UserActivity(models.Model):
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return str(self.is_active)
    
    class Meta:
        verbose_name_plural = "UserActivity"
