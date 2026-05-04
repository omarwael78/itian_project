from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import RedirectView

def dummy_login(request): return HttpResponse("<h1>Login Page Tag</h1>")
def dummy_logout(request): return HttpResponse("<h1>Logout Tag</h1>")
def dummy_register(request): return HttpResponse("<h1>Registration Tag</h1>")

urlpatterns = [
    path('', RedirectView.as_view(url='/trainees/'), name='home'),
    path('admin/', admin.site.urls),
    path('trainees/', include('trainee.urls')),
    path('courses/', include('course.urls')),
    
    path('login/', dummy_login, name='login'),
    path('logout/', dummy_logout, name='logout'),
    path('register/', dummy_register, name='register'),
]