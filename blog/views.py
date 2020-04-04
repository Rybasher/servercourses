from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'blog/courses.html', {'courses': courses})


def courses_detail(request, slug):
    course = Course.objects.get(slug__iexact=slug)
    # search_query = request.GET.get('search', '')
    # if search_query:
    #     posts = course.posts.filter(Q(title__contains=search_query) | Q(content__icontains=search_query))
    #
    # else:
    #     posts = course.posts.all()
    posts = course.posts.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())

    else:
        prev_url = ''

    if page.has_next():
        last_url = '?page={}'.format(paginator.page_range[-1])
        next_url = '?page={}'.format(page.next_page_number())

    else:
        next_url = ''
        last_url = ''
    return render(request, 'blog/course_detail.html', {'course': course, 'posts': posts, 'is_paginated': is_paginated,
                                                       'page_object': page, 'prev_url': prev_url, 'next_url': next_url,
                                                       'last_url': last_url})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'blog/post_detail.html', {'post': post})
