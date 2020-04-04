from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'blog/courses.html', {'courses': courses})


def courses_detail(request, slug):
    course = Course.objects.get(slug__iexact=slug)
    posts = course.posts.all()
    return render(request, 'blog/course_detail.html', {'course': course, 'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'blog/post_detail.html', {'post': post})
