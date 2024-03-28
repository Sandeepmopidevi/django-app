from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='student'),
    path('register/', views.register, name='register')
]