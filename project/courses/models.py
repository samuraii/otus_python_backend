from django.db import models


class Courses(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    subject = models.CharField(max_length=256, unique=False)
    course_display_level_ru = models.CharField(max_length=256, unique=True)
    course_display_level_en = models.CharField(max_length=256, unique=True)
    course_display_topics_ru = models.CharField(max_length=256, unique=True)
    course_display_topics_en = models.CharField(max_length=256, unique=True)
    course_description_ru = models.TextField()
    course_description_en = models.TextField()
    course_url = models.CharField(max_length=256)

    def __str__(self):
        return self.course_url
