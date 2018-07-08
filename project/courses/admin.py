from django.contrib import admin
from courses.models import Course, CourseDescription

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseDescription)
