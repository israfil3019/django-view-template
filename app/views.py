from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):

    print(request.method)

    return HttpResponse("Hello World!")
