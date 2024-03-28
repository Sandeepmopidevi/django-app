from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('student.urls')),
    path('students/', include('student.urls')),
    path('register/', include('student.urls')),
    path('cookies/', include('cookies.urls')),
    path('set_cookie/', include('cookies.urls')),
    path('get_cookie/', include('cookies.urls')),
    path('session/', include('session.urls')),
    path('admin/', admin.site.urls),
    
]
