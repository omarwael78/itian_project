from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from trainee.views import LoginView, RegisterView


def home_redirect(request):
    return redirect('trainee_list' if request.user.is_authenticated else 'login')

urlpatterns = [
    path('', home_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('trainees/', include('trainee.urls')),
    path('courses/', include('course.urls')),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)