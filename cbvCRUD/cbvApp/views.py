from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cbvApp.models import Student
from django.urls import reverse_lazy

# Create your views here.
class StudentListView(ListView):
    model =Student

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName', 'lastName', 'testScore')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('testScore',)

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students')