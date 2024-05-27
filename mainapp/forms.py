from django import forms

from .models import Student








class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels= {
            'dob': 'Date of Birth',
            'adm_no':'Admission Number'
        }
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }





class LoginForm(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)