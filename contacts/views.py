from django.shortcuts import render
from .models import *
# Create your views here.


def contacts_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'contacts/contacts_list.html', {'teachers': teachers})

