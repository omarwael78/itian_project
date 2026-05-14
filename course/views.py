from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


@login_required(login_url='login')
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


@login_required(login_url='login')
def add_course(request):
    if request.method == 'POST':
        # منطق بسيط لإضافة كورس جديد من خلال الفورم
        course_name = request.POST.get('name')
        if course_name:
            Course.objects.create(name=course_name)
            return redirect('course_list')
    return render(request, 'add_course.html')


@login_required(login_url='login')
def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            course.name = new_name
            course.save()
            return redirect('course_list')
    return render(request, 'update_course.html', {'course': course})


@login_required(login_url='login')
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')