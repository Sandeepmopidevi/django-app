from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie Set!")
    response.set_cookie('username', 'sandeep')
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'GUEST')
    return HttpResponse("Hello: " + username)
