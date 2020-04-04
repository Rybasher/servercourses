from django.shortcuts import render
from .models import *
from blog.models import Course
# Create your views here.


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'childs/courses.html', {'course': courses})


def childs_list(request, slug):
    course = Course.objects.get(slug__iexact=slug)
    childs = course.childs.all()
    return render(request, 'childs/childs_list.html', {'childs': childs})
