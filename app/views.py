from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(r):
    return HttpResponse("<h1>Jenkins Deployment CI/CD</h1>")