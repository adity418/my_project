from django import forms
from courApp.models import Course

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'