from django.shortcuts import render
from django.http import HttpResponse
from .models import student_data,sample_data

def home(request):
    return render(request, 'first.html')

def students(request):
    students = student_data.objects.all()
    return render(request, 'student.html', {'students': students})

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        
        sample_data.objects.create(
            firstname=first_name,
            lastname=last_name,
            email=email,
            gender=gender
        )
        return HttpResponse('Data has been saved successfully')
    else:
        return render(request, 'details.html', {'register': sample_data.objects.all()})
