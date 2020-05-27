from django.http import HttpResponse
from django.shortcuts import render

def about(req):
    return render(req, 'about.html', { 'title': 'About' })
