from django.shortcuts import render
from django.http import HttpResponse

def trainee_list(request):
    trainees = [
        {'id': 1, 'name': 'Omar Wael', 'track': 'Python & Systems'},
        {'id': 2, 'name': 'Ahmed', 'track': 'Frontend'}
    ]
    return render(request, 'trainee_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == 'POST':
        return HttpResponse("<h1>Redirect: trainee_list (After Add)</h1>")
    return render(request, 'add_trainee.html')

def update_trainee(request, id):
    return HttpResponse(f"<h1>Redirect: trainee_list (After Update Trainee ID: {id})</h1>")

def delete_trainee(request, id):
    return HttpResponse(f"<h1>Redirect: trainee_list (After Delete Trainee ID: {id})</h1>")