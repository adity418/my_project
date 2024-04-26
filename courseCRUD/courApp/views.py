from django.shortcuts import render, redirect
from courApp.models import Course
from courApp.forms import CourseForm

# Create your views here.
def getCourse(request):
    courses = Course.objects.all()
    return render(request, 'courApp/index.html',{'courses':courses})

def createCourse(request):
    form = CourseForm()
    if request.method =='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'courApp/create.html',{'form':form})

def deleteCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

def updateCourse(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance=course)
    if request.method =='POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'courApp/update.html', {'form':form})
            