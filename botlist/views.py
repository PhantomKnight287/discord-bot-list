from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
# Create your views here.


def index(req):
    return render(req, 'index.html')


def submitBot(req: HttpRequest):
    return render(req, 'submit.html')
