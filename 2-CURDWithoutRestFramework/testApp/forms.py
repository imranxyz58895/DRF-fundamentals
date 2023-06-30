from django import forms
from . import models 


class EmployeeModelForm(forms.ModelForm):
    def clean_salary(self):
        salary_data = self.cleaned_data['salary']
        return salary_data

    class Meta:
        model = models.Employee 
        fields = '__all__'