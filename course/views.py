from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def course_list(request):
    courses = [{'id': 1, 'name': 'Django Basics'}, {'id': 2, 'name': 'Bash Scripting'}]
    return render(request, 'course_list.html', {'courses': courses})


@login_required(login_url='login')
def add_course(request):
    if request.method == 'POST':
        return HttpResponse("<h1>Redirect: courselist (After Add)</h1>")
    return render(request, 'add_course.html')


@login_required(login_url='login')
def update_course(request, id):
    return HttpResponse(f"<h1>Redirect: courselist (After Update Course ID: {id})</h1>")


@login_required(login_url='login')
def delete_course(request, id):
    return HttpResponse(f"<h1>Redirect: courselist (After Delete Course ID: {id})</h1>")