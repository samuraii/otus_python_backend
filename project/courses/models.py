from django.db import models


class Course(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    course_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.course_name


class CourseDescription(models.Model):
    id = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
    course_display_name_ru = models.CharField(max_length=256, unique=True)
    course_display_name_en = models.CharField(max_length=256, unique=True)
    course_description = models.TextField(unique=True)
    course_url = models.TextField()
