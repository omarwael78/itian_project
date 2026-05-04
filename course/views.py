from django.shortcuts import render
from django.http import HttpResponse

def course_list(request):
    courses = [{'id': 1, 'name': 'Django Basics'}, {'id': 2, 'name': 'Bash Scripting'}]
    return render(request, 'course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        return HttpResponse("<h1>Redirect: courselist (After Add)</h1>")
    return render(request, 'add_course.html')

def update_course(request, id):
    return HttpResponse(f"<h1>Redirect: courselist (After Update Course ID: {id})</h1>")

def delete_course(request, id):
    return HttpResponse(f"<h1>Redirect: courselist (After Delete Course ID: {id})</h1>")