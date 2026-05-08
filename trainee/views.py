from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee

def trainee_list(request):
    trainees = Trainee.objects.all() 
    return render(request, 'trainee_list.html', {'trainees': trainees})

def trainee_detail(request, id):
    trainee = get_object_or_404(Trainee, id=id) 
    return render(request, 'trainee_detail.html', {'trainee': trainee})

def add_trainee(request):
    if request.method == 'POST':
        t_name = request.POST.get('name')
        t_track = request.POST.get('track')
        Trainee.objects.create(name=t_name, track=t_track)
        return redirect('trainee_list') 
    return render(request, 'add_trainee.html')

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete() 
    return redirect('trainee_list')