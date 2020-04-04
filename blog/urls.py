from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = "blog"

urlpatterns = [
    path('', index, name='index'),
    path('courses/', courses_list, name='courses_list'),
    path('courses/<str:slug>', courses_detail, name='courses_detail'),
    path('post/<str:slug>', post_detail, name='post_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

