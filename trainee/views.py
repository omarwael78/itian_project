from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeModelForm 

def trainee_list(request):
    trainees = Trainee.objects.all() 
    return render(request, 'trainee_list.html', {'trainees': trainees})

def trainee_detail(request, id):
    trainee = get_object_or_404(Trainee, id=id) 
    return render(request, 'trainee_detail.html', {'trainee': trainee})

def add_trainee(request):
    if request.method == 'POST':
        t_name = request.POST.get('trainee_name')
        t_course_id = request.POST.get('course_id') 
        
        Trainee.objects.create(name=t_name, course_id=t_course_id)
        
        return redirect('trainee_list')
    
    from course.models import Course
    all_courses = Course.objects.all()
    return render(request, 'add_trainee.html', {'courses': all_courses})

def add_trainee_v2(request):
    if request.method == 'POST':
        form = TraineeModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect('trainee_list')
    else:
        form = TraineeModelForm()
    
    return render(request, 'add_trainee_v2.html', {'form': form})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete() 
    return redirect('trainee_list')