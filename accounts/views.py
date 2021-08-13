from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def test_view(request):
    return HttpResponse('<h1>It works!</h1>')
