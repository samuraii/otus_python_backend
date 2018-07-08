from django.shortcuts import render
from courses.models import CourseDescription, Course


# Create your views here.
def index(request):
    courses = CourseDescription.objects.all()
    params = {'courses': courses}
    return render(request, 'courses/index.html', context=params)


def course_page(request):
    course_from_path = request.path.split('/')[-1]
    course_id = Course.objects.filter(course_name=course_from_path).get().id
    course_data = CourseDescription.objects.filter(id=course_id).get()
    params = {'course': course_data}
    return render(request, 'courses/course_page.html', context=params)
