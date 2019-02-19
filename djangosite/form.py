from django import forms  
from djangosite.models import Student,Employee


class StuForm(forms.ModelForm):
	firstname =forms.CharField(label="Enter first name",max_length=50)
	lastname =forms.CharField(label="Enter last name",max_length=10)
	email =forms.EmailField(label="Enter Email")
	file = forms.FileField()

	class Meta:
		model = Student
		fields = "__all__"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"