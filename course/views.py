from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Course
from .serializers import CourseSerializer


# ── REST API ────────────────────────────────────────────────────────────────
class CourseViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for Course via JWT-protected REST API.
    Endpoints:
        GET    /api/courses/          – list all courses
        POST   /api/courses/          – create a course
        GET    /api/courses/{id}/     – retrieve a course
        PUT    /api/courses/{id}/     – full update
        PATCH  /api/courses/{id}/     – partial update
        DELETE /api/courses/{id}/     – delete
    All endpoints require a valid JWT Bearer token.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


# ── Template-based views ─────────────────────────────────────────────────────
@login_required(login_url='login')
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


@login_required(login_url='login')
def add_course(request):
    if request.method == 'POST':
        course_title = request.POST.get('title')
        if course_title:
            Course.objects.create(title=course_title)
            return redirect('course_list')
    return render(request, 'add_course.html')


@login_required(login_url='login')
def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title:
            course.title = new_title
            course.save()
            return redirect('course_list')
    return render(request, 'update_course.html', {'course': course})


@login_required(login_url='login')
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')