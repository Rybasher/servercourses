from django.urls import path
from .views import *

app_name = 'childs'

urlpatterns = [
    path('courses_list/', courses_list, name='coursess_list'),
    path('child_list/<str:slug>', childs_list, name='child_list')
]