# session/views.py
from django.http import HttpResponse

def set_session(request):
    request.session['username'] = 'Sandeep'
    return HttpResponse("Session Set!")

def get_session(request):
    username = request.session.get('username', 'GUEST')
    return HttpResponse("Hello: " + username)
