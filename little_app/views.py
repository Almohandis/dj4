from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(req):
    data = {"text": "hello world", "number": 100, "data": 45}
    return render(req, "little_app/index.html", data)


def other(req):
    data = {"text": "hello world", "number": 100, "data": 45}
    return render(req, "little_app/other.html", data)
