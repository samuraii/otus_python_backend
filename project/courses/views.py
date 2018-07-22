from django.shortcuts import render
from courses.models import Courses


# Create your views here.
def index(request):
    courses = Courses.objects.all()
    params = {'courses': courses}
    return render(request, 'courses/index.html', context=params)


def course_page(request):
    course_from_path = request.path.split('/')[-1]
    # course_data = CourseDescription.objects.filter(id=course_id).get()
    course_data = Courses.objects.filter(course_url=course_from_path).get()
    params = {'course': course_data}
    return render(request, 'courses/course_page.html', context=params)
