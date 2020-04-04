from django.urls import path
from .views import *

app_name = 'contacts'

urlpatterns = [
    path('contacts', contacts_list, name='contacts_list')
]