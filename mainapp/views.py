from django.shortcuts import render , redirect, get_object_or_404
from mainapp.models import Student
from mainapp.forms import StudentForm , LoginForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def home (request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Student successfully saved')
            return redirect('all_students')
    else:
        form = StudentForm()
    return render(request, 'student.html', {'form': form})



@login_required
def all_students(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'all_students.html', {'students':students})



@login_required
def student_details(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'student_details.html', {'student':student})


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    messages.warning(request, 'Student delete permanently')
    return redirect ('all_students')


@login_required
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST , request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student update successsfully')
            return redirect('student_details', student_id)
    else:
        form = StudentForm(instance=student)
        return render (request, 'update.html', {'form':form})


@login_required
def search_students(request):
    search_word = request.GET['search_word']
    students = Student.objects.filter(Q(name__icontains=search_word) | Q(adm_no__icontains=search_word))
    return render(request, 'all_students.html', {'students': students})


def signin(request):
    if request.method =='GET':
        form = LoginForm()
        return render (request, 'login.html', {'form':form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
             username= form.cleaned_data['username']
             password = form.cleaned_data['password']
             user = authenticate(request, username=username, password=password)
             if user:
                    login(request, user)
                    return redirect('home')
             messages.error(request, 'Invalid username or password')
             return render(request, 'login.html', {'form': form})


@login_required
def signout(request):
    logout(request)
    return redirect('signin')