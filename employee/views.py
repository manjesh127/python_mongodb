from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Employee


def home(request):
    emoloyee_data = Employee.objects.all()
    for field in emoloyee_data:
        print('name student is', field.name)
    return HttpResponse('this url is working')
