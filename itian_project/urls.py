from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from trainee.views import LoginView, RegisterView, TraineeViewSet 
from course.views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course-api')
router.register(r'trainees', TraineeViewSet, basename='trainee-api')

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

    path('api/', include(router.urls)), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)