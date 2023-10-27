from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def hello(request: HttpRequest) -> HttpResponse:
    HttpResponse("Hello World!")